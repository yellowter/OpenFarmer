# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(775, 517)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Administrator/.designer/backup/favicon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(20, 17, 41, 16))
        self.label_1.setObjectName("label_1")
        self.edit_account = QtWidgets.QLineEdit(Dialog)
        self.edit_account.setGeometry(QtCore.QRect(50, 15, 116, 20))
        self.edit_account.setObjectName("edit_account")
        self.plain_text_edit = QtWidgets.QPlainTextEdit(Dialog)
        self.plain_text_edit.setGeometry(QtCore.QRect(20, 260, 741, 221))
        self.plain_text_edit.setReadOnly(True)
        self.plain_text_edit.setMaximumBlockCount(100)
        self.plain_text_edit.setObjectName("plain_text_edit")
        self.button_start = QtWidgets.QPushButton(Dialog)
        self.button_start.setGeometry(QtCore.QRect(650, 30, 101, 41))
        self.button_start.setObjectName("button_start")
        self.edit_proxy = QtWidgets.QLineEdit(Dialog)
        self.edit_proxy.setGeometry(QtCore.QRect(265, 15, 101, 20))
        self.edit_proxy.setObjectName("edit_proxy")
        self.checkbox_proxy = QtWidgets.QCheckBox(Dialog)
        self.checkbox_proxy.setGeometry(QtCore.QRect(190, 15, 71, 20))
        self.checkbox_proxy.setChecked(False)
        self.checkbox_proxy.setObjectName("checkbox_proxy")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(18, 110, 103, 124))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkbox_withdraw = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkbox_withdraw.setChecked(False)
        self.checkbox_withdraw.setObjectName("checkbox_withdraw")
        self.verticalLayout.addWidget(self.checkbox_withdraw)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_11)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.need_fwf = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.need_fwf.setObjectName("need_fwf")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.need_fwf)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.need_fwg = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.need_fwg.setObjectName("need_fwg")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.need_fwg)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9)
        self.withdraw_min = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.withdraw_min.setObjectName("withdraw_min")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.withdraw_min)
        self.need_fww = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.need_fww.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.need_fww.setObjectName("need_fww")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.need_fww)
        self.verticalLayout.addLayout(self.formLayout)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(142, 110, 187, 111))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkbox_auto_deposit = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkbox_auto_deposit.setChecked(False)
        self.checkbox_auto_deposit.setObjectName("checkbox_auto_deposit")
        self.verticalLayout_3.addWidget(self.checkbox_auto_deposit)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.fww_min = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.fww_min.setObjectName("fww_min")
        self.gridLayout.addWidget(self.fww_min, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 0, 4, 1, 1)
        self.fwf_min = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.fwf_min.setObjectName("fwf_min")
        self.gridLayout.addWidget(self.fwf_min, 0, 3, 1, 1)
        self.fwg_min = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.fwg_min.setObjectName("fwg_min")
        self.gridLayout.addWidget(self.fwg_min, 0, 5, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.deposit_fww = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.deposit_fww.setObjectName("deposit_fww")
        self.gridLayout_2.addWidget(self.deposit_fww, 0, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 0, 0, 1, 1)
        self.deposit_fwg = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.deposit_fwg.setObjectName("deposit_fwg")
        self.gridLayout_2.addWidget(self.deposit_fwg, 0, 5, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 0, 4, 1, 1)
        self.deposit_fwf = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.deposit_fwf.setObjectName("deposit_fwf")
        self.gridLayout_2.addWidget(self.deposit_fwf, 0, 3, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 0, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(-44, 90, 0, 20))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(348, 110, 171, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.checkbox_sell_corn = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkbox_sell_corn.setChecked(False)
        self.checkbox_sell_corn.setObjectName("checkbox_sell_corn")
        self.gridLayout_3.addWidget(self.checkbox_sell_corn, 0, 0, 1, 1)
        self.remaining_corn_num = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.remaining_corn_num.setObjectName("remaining_corn_num")
        self.gridLayout_3.addWidget(self.remaining_corn_num, 0, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 1, 1, 1)
        self.checkbox_sell_barley = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkbox_sell_barley.setChecked(False)
        self.checkbox_sell_barley.setObjectName("checkbox_sell_barley")
        self.gridLayout_3.addWidget(self.checkbox_sell_barley, 1, 0, 1, 1)
        self.checkbox_sell_milk = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkbox_sell_milk.setChecked(False)
        self.checkbox_sell_milk.setObjectName("checkbox_sell_milk")
        self.gridLayout_3.addWidget(self.checkbox_sell_milk, 2, 0, 1, 1)
        self.checkbox_sell_egg = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkbox_sell_egg.setChecked(False)
        self.checkbox_sell_egg.setObjectName("checkbox_sell_egg")
        self.gridLayout_3.addWidget(self.checkbox_sell_egg, 3, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 1, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 2, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 3, 1, 1, 1)
        self.remaining_barley_num = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.remaining_barley_num.setObjectName("remaining_barley_num")
        self.gridLayout_3.addWidget(self.remaining_barley_num, 1, 2, 1, 1)
        self.remaining_milk_num = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.remaining_milk_num.setObjectName("remaining_milk_num")
        self.gridLayout_3.addWidget(self.remaining_milk_num, 2, 2, 1, 1)
        self.remaining_egg_num = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.remaining_egg_num.setObjectName("remaining_egg_num")
        self.gridLayout_3.addWidget(self.remaining_egg_num, 3, 2, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(490, 10, 131, 74))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.spinbox_min_durability = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.spinbox_min_durability.setKeyboardTracking(True)
        self.spinbox_min_durability.setSuffix("")
        self.spinbox_min_durability.setMaximum(2000)
        self.spinbox_min_durability.setSingleStep(10)
        self.spinbox_min_durability.setProperty("value", 20)
        self.spinbox_min_durability.setObjectName("spinbox_min_durability")
        self.gridLayout_4.addWidget(self.spinbox_min_durability, 2, 1, 1, 1)
        self.spinbox_energy = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.spinbox_energy.setMaximum(9000)
        self.spinbox_energy.setSingleStep(100)
        self.spinbox_energy.setProperty("value", 500)
        self.spinbox_energy.setObjectName("spinbox_energy")
        self.gridLayout_4.addWidget(self.spinbox_energy, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 2, 0, 1, 1)
        self.spinbox_min_energy = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.spinbox_min_energy.setEnabled(True)
        self.spinbox_min_energy.setMaximum(9000)
        self.spinbox_min_energy.setSingleStep(10)
        self.spinbox_min_energy.setProperty("value", 50)
        self.spinbox_min_energy.setObjectName("spinbox_min_energy")
        self.gridLayout_4.addWidget(self.spinbox_min_energy, 1, 1, 1, 1)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(538, 110, 111, 116))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkbox_auto_plant = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.checkbox_auto_plant.setChecked(False)
        self.checkbox_auto_plant.setObjectName("checkbox_auto_plant")
        self.verticalLayout_4.addWidget(self.checkbox_auto_plant)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_21.setObjectName("label_21")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_21)
        self.label_22 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_22.setObjectName("label_22")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_22)
        self.cornseed_num = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.cornseed_num.setObjectName("cornseed_num")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cornseed_num)
        self.barleyseed_num = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.barleyseed_num.setObjectName("barleyseed_num")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.barleyseed_num)
        self.verticalLayout_4.addLayout(self.formLayout_4)
        self.checkbox_buy_barley_seed = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.checkbox_buy_barley_seed.setChecked(False)
        self.checkbox_buy_barley_seed.setObjectName("checkbox_buy_barley_seed")
        self.verticalLayout_4.addWidget(self.checkbox_buy_barley_seed)
        self.checkbox_buy_corn_seed = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.checkbox_buy_corn_seed.setChecked(False)
        self.checkbox_buy_corn_seed.setObjectName("checkbox_buy_corn_seed")
        self.verticalLayout_4.addWidget(self.checkbox_buy_corn_seed)
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(123, 110, 16, 111))
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(330, 110, 16, 111))
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(520, 110, 16, 111))
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_24 = QtWidgets.QLabel(Dialog)
        self.label_24.setGeometry(QtCore.QRect(20, 490, 561, 16))
        self.label_24.setObjectName("label_24")
        self.line_6 = QtWidgets.QFrame(Dialog)
        self.line_6.setGeometry(QtCore.QRect(0, 92, 821, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(669, 110, 85, 62))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkbox_buy_food = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.checkbox_buy_food.setChecked(False)
        self.checkbox_buy_food.setObjectName("checkbox_buy_food")
        self.verticalLayout_2.addWidget(self.checkbox_buy_food)
        self.label_23 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_2.addWidget(self.label_23)
        self.buy_food_num = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.buy_food_num.setObjectName("buy_food_num")
        self.verticalLayout_2.addWidget(self.buy_food_num)
        self.line_7 = QtWidgets.QFrame(Dialog)
        self.line_7.setGeometry(QtCore.QRect(650, 110, 16, 111))
        self.line_7.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_7.setObjectName("line_7")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(20, 73, 461, 16))
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.checkbox_build = QtWidgets.QCheckBox(self.splitter)
        self.checkbox_build.setChecked(False)
        self.checkbox_build.setObjectName("checkbox_build")
        self.checkbox_mining = QtWidgets.QCheckBox(self.splitter)
        self.checkbox_mining.setEnabled(True)
        self.checkbox_mining.setChecked(True)
        self.checkbox_mining.setObjectName("checkbox_mining")
        self.checkbox_chicken = QtWidgets.QCheckBox(self.splitter)
        self.checkbox_chicken.setChecked(False)
        self.checkbox_chicken.setObjectName("checkbox_chicken")
        self.checkbox_plant = QtWidgets.QCheckBox(self.splitter)
        self.checkbox_plant.setChecked(False)
        self.checkbox_plant.setObjectName("checkbox_plant")
        self.checkbox_cow = QtWidgets.QCheckBox(self.splitter)
        self.checkbox_cow.setChecked(False)
        self.checkbox_cow.setObjectName("checkbox_cow")
        self.checkbox_breeding = QtWidgets.QCheckBox(self.splitter)
        self.checkbox_breeding.setChecked(False)
        self.checkbox_breeding.setObjectName("checkbox_breeding")
        self.checkbox_mbs = QtWidgets.QCheckBox(self.splitter)
        self.checkbox_mbs.setChecked(False)
        self.checkbox_mbs.setObjectName("checkbox_mbs")
        self.checkbox_mbs_mint = QtWidgets.QCheckBox(self.splitter)
        self.checkbox_mbs_mint.setChecked(False)
        self.checkbox_mbs_mint.setObjectName("checkbox_mbs_mint")
        self.label_25 = QtWidgets.QLabel(Dialog)
        self.label_25.setGeometry(QtCore.QRect(20, 42, 41, 16))
        self.label_25.setObjectName("label_25")
        self.comboBox_rpc_domain = QtWidgets.QComboBox(Dialog)
        self.comboBox_rpc_domain.setGeometry(QtCore.QRect(50, 40, 201, 22))
        self.comboBox_rpc_domain.setObjectName("comboBox_rpc_domain")
        self.comboBox_rpc_domain.addItem("")
        self.comboBox_rpc_domain.addItem("")
        self.comboBox_rpc_domain.addItem("")
        self.comboBox_rpc_domain.addItem("")
        self.comboBox_rpc_domain.addItem("")
        self.comboBox_rpc_domain.addItem("")
        self.comboBox_rpc_domain.addItem("")
        self.comboBox_rpc_domain.addItem("")
        self.label_26 = QtWidgets.QLabel(Dialog)
        self.label_26.setGeometry(QtCore.QRect(260, 42, 51, 16))
        self.label_26.setObjectName("label_26")
        self.comboBox_assets_domain = QtWidgets.QComboBox(Dialog)
        self.comboBox_assets_domain.setGeometry(QtCore.QRect(310, 40, 161, 22))
        self.comboBox_assets_domain.setObjectName("comboBox_assets_domain")
        self.comboBox_assets_domain.addItem("")
        self.comboBox_assets_domain.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "农民世界助手"))
        self.label_1.setText(_translate("Dialog", "账号:"))
        self.edit_account.setText(_translate("Dialog", "abcde.wam"))
        self.button_start.setText(_translate("Dialog", "启动"))
        self.edit_proxy.setText(_translate("Dialog", "127.0.0.1:1080"))
        self.checkbox_proxy.setText(_translate("Dialog", "启用代理"))
        self.checkbox_withdraw.setText(_translate("Dialog", "5%自动提现"))
        self.label_11.setText(_translate("Dialog", "保留木头"))
        self.label_7.setText(_translate("Dialog", "保留食物"))
        self.need_fwf.setText(_translate("Dialog", "1000"))
        self.label_8.setText(_translate("Dialog", "保留金子"))
        self.need_fwg.setText(_translate("Dialog", "1000"))
        self.label_9.setToolTip(_translate("Dialog", "最少提现数量，3种材料总和"))
        self.label_9.setText(_translate("Dialog", "最少提现?"))
        self.withdraw_min.setText(_translate("Dialog", "500"))
        self.need_fww.setText(_translate("Dialog", "0"))
        self.checkbox_auto_deposit.setText(_translate("Dialog", "自动充值资源"))
        self.label_4.setText(_translate("Dialog", "触发充值："))
        self.fww_min.setText(_translate("Dialog", "0"))
        self.label_13.setText(_translate("Dialog", "肉"))
        self.label_15.setText(_translate("Dialog", "金"))
        self.fwf_min.setText(_translate("Dialog", "200"))
        self.fwg_min.setText(_translate("Dialog", "200"))
        self.label_17.setText(_translate("Dialog", "木"))
        self.label_5.setText(_translate("Dialog", "充值数量："))
        self.deposit_fww.setText(_translate("Dialog", "0"))
        self.label_18.setText(_translate("Dialog", "木"))
        self.deposit_fwg.setText(_translate("Dialog", "200"))
        self.label_19.setText(_translate("Dialog", "金"))
        self.deposit_fwf.setText(_translate("Dialog", "200"))
        self.label_20.setText(_translate("Dialog", "肉"))
        self.checkbox_sell_corn.setText(_translate("Dialog", "卖玉米"))
        self.remaining_corn_num.setText(_translate("Dialog", "0"))
        self.label_10.setText(_translate("Dialog", "保留玉米"))
        self.checkbox_sell_barley.setText(_translate("Dialog", "卖大麦"))
        self.checkbox_sell_milk.setText(_translate("Dialog", "卖牛奶"))
        self.checkbox_sell_egg.setText(_translate("Dialog", "卖鸡蛋"))
        self.label_12.setText(_translate("Dialog", "保留大麦"))
        self.label_14.setText(_translate("Dialog", "保留牛奶"))
        self.label_16.setText(_translate("Dialog", "保留鸡蛋"))
        self.remaining_barley_num.setText(_translate("Dialog", "0"))
        self.remaining_milk_num.setText(_translate("Dialog", "0"))
        self.remaining_egg_num.setText(_translate("Dialog", "0"))
        self.label_2.setText(_translate("Dialog", "能量恢复"))
        self.label_3.setText(_translate("Dialog", "最低能量"))
        self.label_6.setText(_translate("Dialog", "最低耐久度%"))
        self.checkbox_auto_plant.setText(_translate("Dialog", "自动播种"))
        self.label_21.setText(_translate("Dialog", "大麦种子"))
        self.label_22.setText(_translate("Dialog", "玉米种子"))
        self.cornseed_num.setText(_translate("Dialog", "0"))
        self.barleyseed_num.setText(_translate("Dialog", "8"))
        self.checkbox_buy_barley_seed.setText(_translate("Dialog", "自动买大麦种子"))
        self.checkbox_buy_corn_seed.setText(_translate("Dialog", "自动买玉米种子"))
        self.label_24.setText(_translate("Dialog", ""))
        self.checkbox_buy_food.setToolTip(_translate("Dialog", "自动买食物[玉米或大麦]（喂动物食物不够时，触发购买）"))
        self.checkbox_buy_food.setText(_translate("Dialog", "自动买食物"))
        self.label_23.setToolTip(_translate("Dialog", "一次购买的数量"))
        self.label_23.setText(_translate("Dialog", "购买数量："))
        self.buy_food_num.setText(_translate("Dialog", "0"))
        self.checkbox_build.setText(_translate("Dialog", "建造"))
        self.checkbox_mining.setText(_translate("Dialog", "挖矿"))
        self.checkbox_chicken.setText(_translate("Dialog", "养鸡"))
        self.checkbox_plant.setText(_translate("Dialog", "作物浇水"))
        self.checkbox_cow.setText(_translate("Dialog", "养牛"))
        self.checkbox_breeding.setText(_translate("Dialog", "繁殖"))
        self.checkbox_mbs.setText(_translate("Dialog", "会员"))
        self.checkbox_mbs_mint.setText(_translate("Dialog", "会员存储"))
        self.label_25.setText(_translate("Dialog", "节点"))
        self.comboBox_rpc_domain.setItemText(0, _translate("Dialog", "https://api.wax.alohaeos.com"))
        self.comboBox_rpc_domain.setItemText(1, _translate("Dialog", "https://wax.dapplica.io"))
        self.comboBox_rpc_domain.setItemText(2, _translate("Dialog", "https://wax.pink.gg"))
        self.comboBox_rpc_domain.setItemText(3, _translate("Dialog", "https://api.waxsweden.org"))
        self.comboBox_rpc_domain.setItemText(4, _translate("Dialog", "https://wax.dapplica.io"))
        self.comboBox_rpc_domain.setItemText(5, _translate("Dialog", "https://wax.eosphere.io"))
        self.comboBox_rpc_domain.setItemText(6, _translate("Dialog", "https://api.wax.greeneosio.com"))
        self.comboBox_rpc_domain.setItemText(7, _translate("Dialog", "https://wax.cryptolions.io"))
        self.label_26.setText(_translate("Dialog", "原子节点"))
        self.comboBox_assets_domain.setItemText(0, _translate("Dialog", "https://wax.api.atomicassets.io"))
        self.comboBox_assets_domain.setItemText(1, _translate("Dialog", "https://atomic.wax.eosrio.io"))
