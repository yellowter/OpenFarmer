#!/usr/bin/python3
import yaml
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service
import tenacity
from tenacity import stop_after_attempt, wait_fixed, retry_if_exception_type, RetryCallState
import logging
import requests
from requests.exceptions import RequestException
import functools
from decimal import Decimal
from typing import List, Dict
import base64
import logger
import utils
from utils import plat
import res
from res import Resoure, Farming, Token
from datetime import datetime, timedelta
from settings import cfg
from settings import load_user_param, user_param
import os
from logger import log


class FarmerException(Exception):
    pass


class CookieExpireException(FarmerException):
    pass


# 调用智能合约出错，此时应停止并检查日志，不宜反复重试
class TransactException(FarmerException):
    # 有的智能合约错误可以重试,-1为无限重试
    def __init__(self, msg, retry=True, max_retry_times: int = -1):
        super().__init__(msg)
        self.retry = retry
        self.max_retry_times = max_retry_times


# 遇到不可恢复的错误 ,终止程序
class StopException(FarmerException):
    pass


class Status:
    Continue = 1
    Stop = 2


class Farmer:
    # wax rpc
    # url_rpc = "https://api.wax.alohaeos.com/v1/chain/"
    # url_rpc = "https://wax.dapplica.io/v1/chain/"
    # url_table_row = url_rpc + "get_table_rows"
    # 资产API
    # url_assets = "https://wax.api.atomicassets.io/atomicassets/v1/assets"
    # url_assets = "https://atomic.wax.eosrio.io/atomicassets/v1/assets"
    waxjs: str = None
    myjs: str = None
    chrome_data_dir = os.path.abspath(cfg.chrome_data_dir)

    def __init__(self):
        self.url_rpc: str = None
        self.url_table_row: str = None
        self.url_assets: str = None

        self.wax_account: str = None
        self.login_name: str = None
        self.password: str = None
        self.driver: webdriver.Chrome = None
        self.proxy: str = None
        self.http: requests.Session = None
        self.cookies: List[dict] = None
        self.log: logging.LoggerAdapter = log
        # 下一次可以操作东西的时间
        self.next_operate_time: datetime = datetime.max
        # 下一次扫描时间
        self.next_scan_time: datetime = datetime.min
        # 本轮扫描中暂不可操作的东西
        self.not_operational: List[Farming] = []
        # 智能合约连续出错次数
        self.count_error_transact = 0
        # 本轮扫描中作物操作成功个数
        self.count_success_claim = 0
        # 本轮扫描中作物操作失败个数
        self.count_error_claim = 0
        # 本轮开始时的资源数量
        self.resoure: Resoure = None
        self.token: Token = None

    def close(self):
        if self.driver:
            self.log.info("稍等，程序正在退出")
            self.driver.quit()

    def init(self):
        self.url_rpc = user_param.rpc_domain + '/v1/chain/'
        self.url_table_row = user_param.rpc_domain + '/v1/chain/get_table_rows'
        self.url_assets = user_param.assets_domain + '/atomicassets/v1/assets'

        self.log.extra["tag"] = self.wax_account
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        # options.add_argument("--no-sandbox")
        options.add_argument("--disable-extensions")
        options.add_argument("--log-level=3")
        options.add_argument("--disable-logging")
        data_dir = os.path.join(Farmer.chrome_data_dir, self.wax_account)
        options.add_argument("--user-data-dir={0}".format(data_dir))
        if self.proxy:
            options.add_argument("--proxy-server={0}".format(self.proxy))

        # s = Service(plat.driver_path)
        self.driver = webdriver.Chrome(plat.driver_path, options=options)
        self.driver.implicitly_wait(60)
        self.driver.set_script_timeout(60)
        self.http = requests.Session()
        self.http.trust_env = False
        self.http.request = functools.partial(self.http.request, timeout=30)
        if self.proxy:
            self.http.proxies = {
                "http": "http://{0}".format(self.proxy),
                "https": "http://{0}".format(self.proxy),
            }
        http_retry_wrapper = tenacity.retry(wait=wait_fixed(cfg.req_interval), stop=stop_after_attempt(5),
                                            retry=retry_if_exception_type(RequestException),
                                            before_sleep=self.log_retry, reraise=True)
        self.http.get = http_retry_wrapper(self.http.get)
        self.http.post = http_retry_wrapper(self.http.post)

    def inject_waxjs(self):
        # 如果已经注入过就不再注入了
        if self.driver.execute_script("return window.mywax != undefined;"):
            return True

        if not Farmer.waxjs:
            with open("waxjs.js", "r") as file:
                Farmer.waxjs = file.read()
                file.close()
                Farmer.waxjs = base64.b64encode(Farmer.waxjs.encode()).decode()
        if not Farmer.myjs:
            with open("inject.js", "r") as file:
                inject_rpc = "window.mywax = new waxjs.WaxJS({rpcEndpoint: '" + user_param.rpc_domain + "'});"
                Farmer.myjs = inject_rpc + file.read()
                file.close()

        code = "var s = document.createElement('script');"
        code += "s.type = 'text/javascript';"
        code += "s.text = atob('{0}');".format(Farmer.waxjs)
        code += "document.head.appendChild(s);"
        self.driver.execute_script(code)
        self.driver.execute_script(Farmer.myjs)
        return True

    def start(self):
        self.log.info("启动浏览器")
        self.log.info("wax节点: {0}".format(user_param.rpc_domain))
        self.log.info("原子市场节点: {0}".format(user_param.assets_domain))

        self.driver.get("https://play.farmersworld.io/")
        # 等待页面加载完毕
        elem = self.driver.find_element(By.ID, "RPC-Endpoint")
        elem.find_element(By.XPATH, "option[contains(@name, 'https')]")
        wait_seconds = 60
        if self.may_cache_login():
            self.log.info("使用Cache自动登录")
        else:
            wait_seconds = 600
            self.log.info("请在弹出的窗口中手动登录账号")
        # 点击登录按钮，点击WAX云钱包方式登录
        elem = self.driver.find_element(By.CLASS_NAME, "login-button")
        elem.click()
        elem = self.driver.find_element(By.CLASS_NAME, "login-button--text")
        elem.click()
        # 等待登录成功
        self.log.info("等待登录")
        WebDriverWait(self.driver, wait_seconds, 1).until(
            EC.presence_of_element_located((By.XPATH, "//img[@class='navbar-group--icon' and @alt='Map']")))
        # self.driver.find_element(By.XPATH, "//img[@class='navbar-group--icon' and @alt='Map']")
        self.log.info("登录成功,稍等...")
        time.sleep(cfg.req_interval)
        self.inject_waxjs()
        ret = self.driver.execute_script("return window.wax_login();")
        self.log.info("window.wax_login(): {0}".format(ret))
        if not ret[0]:
            raise CookieExpireException("cookie失效")

        time.sleep(cfg.req_interval)

    def may_cache_login(self):
        cookies = self.driver.execute_cdp_cmd("Network.getCookies", {"urls": ["https://all-access.wax.io"]})
        for item in cookies["cookies"]:
            if item.get("name") == "token_id":
                return True
        return False

    def log_retry(self, state: RetryCallState):
        exp = state.outcome.exception()
        if isinstance(exp, RequestException):
            self.log.info("网络错误: {0}".format(exp))
            self.log.info("正在重试: [{0}]".format(state.attempt_number))

    # 获取三种资源的代币余额 FWF FWG FWW
    def get_fw_balance(self) -> Token:
        url = self.url_rpc + "get_currency_balance"
        post_data = {
            "code": "farmerstoken",
            "account": self.wax_account,
            "symbol": None
        }
        resp = self.http.post(url, json=post_data)

        self.log.debug("get_fw_balance:{0}".format(resp.text))
        resp = resp.json()
        balance = Token()
        balance.fwf = 0
        balance.fwg = 0
        balance.fww = 0
        for item in resp:
            sp = item.split(" ")
            if sp[1].upper() == "FWF":
                balance.fwf = Decimal(sp[0])
            elif sp[1].upper() == "FWG":
                balance.fwg = Decimal(sp[0])
            elif sp[1].upper() == "FWW":
                balance.fww = Decimal(sp[0])
        self.log.debug("fw_balance: {0}".format(balance))
        return balance

    # 转账
    def scan_transfer(self):
        self.log.info("开始转移资源")
        token = self.token
        for item in transfer_config.transfer_list:
            if token.fwf < item['transfer_food']:
                self.log.info(f"账号【{item['account']}】FWF不足：钱包剩余FWF【{token.fwf}】，充值数【{item['transfer_food']}】 ")
                continue
            if token.fww < item['transfer_wood']:
                self.log.info(f"账号【{item['account']}】FWW不足：钱包剩余FWW【{token.fww}】，充值数【{item['transfer_wood']}】 ")
                continue
            if token.fwg < item['transfer_gold']:
                self.log.info(f"账号【{item['account']}】FWG不足：钱包剩余FWG【{token.fwg}】，充值数【{item['transfer_gold']}】 ")
                continue
            self.log.info(f"=================转移资源给【{item['account']}】=================")
            self.log.info(f"金币【{item['transfer_gold']}】 木头【{item['transfer_wood']}】 食物【{item['transfer_food']}】 ")
            self.do_transfer(item['transfer_food'], item['transfer_gold'], item['transfer_wood'], item['account'])
            token.fwf -= item['transfer_food']
            token.fww -= item['transfer_wood']
            token.fwg -= item['transfer_gold']
            self.log.info(f"钱包剩余:FWG【{token.fwg}】 FWW【{token.fww}】 FWF【{token.fwf}】 ")
            self.log.info("================================================================")

        # self.do_transfer(transfer_food, transfer_gold, transfer_wood, account)
        # self.log.info(f"转账：金币【{transfer_gold}】 木头【{transfer_wood}】 食物【{transfer_food}】 ")

        return True

    # 转账
    def do_transfer(self, food, gold, wood, account):
        self.log.info("正在转移资源{0}".format(account))
        # format(1.23456, '.4f')
        quantities = []
        if food > 0:
            food = format(food, '.4f')
            quantities.append(food + " FWF")
        if gold > 0:
            gold = format(gold, '.4f')
            quantities.append(gold + " FWG")
        if wood > 0:
            wood = format(wood, '.4f')
            quantities.append(wood + " FWW")
        # quantities格式：1.0000 FWW
        transaction = {
            "actions": [{
                "account": "farmerstoken",
                "name": "transfers",
                "authorization": [{
                    "actor": self.wax_account,
                    "permission": "active",
                }],
                "data": {
                    "from": self.wax_account,
                    "to": account,
                    "quantities": quantities,
                    "memo": "deposit",
                },
            }],
        }
        self.wax_transact(transaction)
        self.log.info("转账完成{0}".format(account))

    def scan_resource(self):

        self.token = self.get_fw_balance()
        self.log.info(f"主账号资源：FWG【{self.token.fwg}】 FWW【{self.token.fww}】 FWF【{self.token.fwf}】")

    def reset_before_scan(self):
        self.not_operational.clear()
        self.count_success_claim = 0
        self.count_error_claim = 0

    # 签署交易(只许成功，否则抛异常）
    def wax_transact(self, transaction: dict):
        self.inject_waxjs()
        self.log.info("begin transact: {0}".format(transaction))
        try:
            success, result = self.driver.execute_script("return window.wax_transact(arguments[0]);", transaction)
            if success:
                self.log.info("transact ok, transaction_id: [{0}]".format(result["transaction_id"]))
                self.log.debug("transact result: {0}".format(result))
                return result
            else:
                if "is greater than the maximum billable" in result:
                    self.log.error("CPU资源不足，可能需要质押更多WAX，一般为误报，稍后重试 maximum")
                elif "estimated CPU time (0 us) is not less than the maximum billable CPU time for the transaction (0 us)" in result:
                    self.log.error("CPU资源不足，可能需要质押更多WAX，一般为误报，稍后重试 estimated")
                else:
                    self.log.error("transact error: {0}".format(result))
                raise TransactException(result)

        except WebDriverException as e:
            self.log.error("transact error: {0}".format(e))
            self.log.exception(str(e))
            raise TransactException(result)

    # 检查正在培养的作物， 返回值：是否继续运行程序
    def scan_all(self) -> int:
        status = Status.Continue
        try:
            self.reset_before_scan()
            self.scan_resource()
            time.sleep(cfg.req_interval)

            self.scan_transfer()
            time.sleep(cfg.req_interval)
            self.log.info("程序运行结束")

        except TransactException as e:
            # self.log.exception("智能合约调用出错")
            if not e.retry:
                return Status.Stop
            self.count_error_transact += 1
            self.log.error("合约调用异常【{0}】次".format(self.count_error_transact))
            if self.count_error_transact >= e.max_retry_times and e.max_retry_times != -1:
                self.log.error("合约连续调用异常")
                return Status.Stop
            self.next_scan_time = datetime.now() + cfg.min_scan_interval
        except CookieExpireException as e:
            self.log.exception(str(e))
            self.log.error("Cookie失效，请手动重启程序并重新登录")
            return Status.Stop
        except StopException as e:
            self.log.exception(str(e))
            self.log.error("不可恢复错误，请手动处理，然后重启程序并重新登录")
            return Status.Stop
        except FarmerException as e:
            self.log.exception(str(e))
            self.log.error("常规错误，稍后重试")
            self.next_scan_time = datetime.now() + cfg.min_scan_interval
        except Exception as e:
            self.log.exception(str(e))
            self.log.error("常规错误，稍后重试")
            self.next_scan_time = datetime.now() + cfg.min_scan_interval

        return status

    def run_forever(self):
        status = self.scan_all()
        if status == Status.Stop:
            self.close()
            self.log.info("程序已停止，请检查日志后手动重启程序")
            return 1


class transfer_config:
    transfer_list: list = []


def run(config_file: str, transfer_yml: str):
    with open(config_file, "r", encoding="utf8") as file:
        user: dict = yaml.load(file, Loader=yaml.FullLoader)
        file.close()
    load_user_param(user)
    with open(transfer_yml, "r", encoding="utf8") as file:
        transfer_dict: dict = yaml.load(file, Loader=yaml.FullLoader)
        transfer_config.transfer_list = transfer_dict.get("list", [])
        file.close()

    logger.init_loger(user_param.wax_account)
    log.info("=======批量转账功能=======")
    log.info("项目开源地址：https://github.com/lintan/OpenFarmer")
    log.info("WAX账号: {0}".format(user_param.wax_account))
    utils.clear_orphan_webdriver()
    farmer = Farmer()
    farmer.wax_account = user_param.wax_account
    if user_param.use_proxy:
        farmer.proxy = user_param.proxy
        log.info("use proxy: {0}".format(user_param.proxy))
    farmer.init()
    farmer.start()
    log.info("开始自动化")
    return farmer.run_forever()


def main():
    try:
        user_yml = "user.yml"
        transfer_yml = "transfer.yml"
        run(user_yml, transfer_yml)
    except Exception:
        log.exception("start error")
    input()


if __name__ == '__main__':
    main()
