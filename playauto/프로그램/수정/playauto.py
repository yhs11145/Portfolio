# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playauto.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import sys,os,time
from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import win32com.client

if getattr(sys, 'frozen', False):
    Chrome_path = os.path.join(sys._MEIPASS, "ChromeDriver.exe")
    driver = webdriver.Chrome(Chrome_path)
else:
    driver=webdriver.Chrome()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1119, 495)
        font = QtGui.QFont()
        font.setFamily("D2Coding")
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 1071, 461))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.tab_3)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(20, 20, 661, 171))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.DeliveryCombo = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.DeliveryCombo.setObjectName("DeliveryCombo")
        self.DeliveryCombo.addItem("")
        self.DeliveryCombo.addItem("")
        self.DeliveryCombo.addItem("")
        self.DeliveryCombo.addItem("")
        self.DeliveryCombo.addItem("")
        self.DeliveryCombo.addItem("")
        self.DeliveryCombo.addItem("")
        self.DeliveryCombo.addItem("")
        self.gridLayout_4.addWidget(self.DeliveryCombo, 2, 2, 1, 1)
        self.OKButton = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.OKButton.setObjectName("OKButton")
        self.gridLayout_4.addWidget(self.OKButton, 3, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_4.addWidget(self.comboBox, 0, 2, 1, 2)
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_2, 1, 2, 1, 2)
        self.StateCombo = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.StateCombo.setObjectName("StateCombo")
        self.StateCombo.addItem("")
        self.StateCombo.addItem("")
        self.StateCombo.addItem("")
        self.StateCombo.addItem("")
        self.StateCombo.addItem("")
        self.StateCombo.addItem("")
        self.StateCombo.addItem("")
        self.StateCombo.addItem("")
        self.StateCombo.addItem("")
        self.gridLayout_4.addWidget(self.StateCombo, 2, 3, 1, 1)
        self.IDEdit2 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.IDEdit2.setObjectName("IDEdit2")
        self.gridLayout_4.addWidget(self.IDEdit2, 0, 1, 1, 1)
        self.PWEdit2 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.PWEdit2.setObjectName("PWEdit2")
        self.gridLayout_4.addWidget(self.PWEdit2, 1, 1, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_41.setObjectName("label_41")
        self.gridLayout_4.addWidget(self.label_41, 0, 0, 1, 1)
        self.RegisterCombo = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.RegisterCombo.setObjectName("RegisterCombo")
        self.RegisterCombo.addItem("")
        self.RegisterCombo.addItem("")
        self.RegisterCombo.addItem("")
        self.RegisterCombo.addItem("")
        self.RegisterCombo.addItem("")
        self.RegisterCombo.addItem("")
        self.RegisterCombo.addItem("")
        self.RegisterCombo.addItem("")
        self.gridLayout_4.addWidget(self.RegisterCombo, 2, 1, 1, 1)
        self.ShoppingCombo = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.ShoppingCombo.setObjectName("ShoppingCombo")
        self.ShoppingCombo.addItem("")
        self.ShoppingCombo.addItem("")
        self.ShoppingCombo.addItem("")
        self.ShoppingCombo.addItem("")
        self.ShoppingCombo.addItem("")
        self.ShoppingCombo.addItem("")
        self.ShoppingCombo.addItem("")
        self.ShoppingCombo.addItem("")
        self.ShoppingCombo.addItem("")
        self.ShoppingCombo.addItem("")
        self.ShoppingCombo.addItem("")
        self.ShoppingCombo.addItem("")
        self.gridLayout_4.addWidget(self.ShoppingCombo, 2, 0, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_42.setObjectName("label_42")
        self.gridLayout_4.addWidget(self.label_42, 1, 0, 1, 1)
        self.NumberCombo = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.NumberCombo.setObjectName("NumberCombo")
        self.NumberCombo.addItem("")
        self.NumberCombo.addItem("")
        self.NumberCombo.addItem("")
        self.NumberCombo.addItem("")
        self.NumberCombo.addItem("")
        self.NumberCombo.addItem("")
        self.NumberCombo.addItem("")
        self.gridLayout_4.addWidget(self.NumberCombo, 2, 4, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 60, 323, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.DDSButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.DDSButton.setObjectName("DDSButton")
        self.horizontalLayout.addWidget(self.DDSButton)
        self.DSSButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.DSSButton.setObjectName("DSSButton")
        self.horizontalLayout.addWidget(self.DSSButton)
        self.DBSButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.DBSButton.setObjectName("DBSButton")
        self.horizontalLayout.addWidget(self.DBSButton)
        self.DPRICEButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.DPRICEButton.setObjectName("DPRICEButton")
        self.horizontalLayout.addWidget(self.DPRICEButton)
        self.DExcelEdit = QtWidgets.QLineEdit(self.tab2)
        self.DExcelEdit.setGeometry(QtCore.QRect(100, 20, 451, 20))
        self.DExcelEdit.setObjectName("DExcelEdit")
        self.label_20 = QtWidgets.QLabel(self.tab2)
        self.label_20.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.label_20.setObjectName("label_20")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(360, 50, 191, 92))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_2.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_2.addWidget(self.label_16)
        self.label_26 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_2.addWidget(self.label_26)
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_2.addWidget(self.label_19)
        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.PANButton = QtWidgets.QPushButton(self.tab3)
        self.PANButton.setGeometry(QtCore.QRect(70, 60, 75, 23))
        self.PANButton.setObjectName("PANButton")
        self.PANText = QtWidgets.QTextBrowser(self.tab3)
        self.PANText.setGeometry(QtCore.QRect(210, 20, 401, 331))
        self.PANText.setObjectName("PANText")
        self.tabWidget.addTab(self.tab3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(50, 130, 332, 80))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.GE2Button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.GE2Button.setObjectName("GE2Button")
        self.gridLayout_2.addWidget(self.GE2Button, 0, 3, 1, 1)
        self.GE1Button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.GE1Button.setObjectName("GE1Button")
        self.gridLayout_2.addWidget(self.GE1Button, 0, 2, 1, 1)
        self.AE1Button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.AE1Button.setObjectName("AE1Button")
        self.gridLayout_2.addWidget(self.AE1Button, 0, 0, 1, 1)
        self.AE2Button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.AE2Button.setObjectName("AE2Button")
        self.gridLayout_2.addWidget(self.AE2Button, 0, 1, 1, 1)
        self.NHButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.NHButton.setObjectName("NHButton")
        self.gridLayout_2.addWidget(self.NHButton, 1, 0, 1, 1)
        self.InterparkButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.InterparkButton.setObjectName("InterparkButton")
        self.gridLayout_2.addWidget(self.InterparkButton, 1, 1, 1, 1)
        self.BunButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.BunButton.setObjectName("BunButton")
        self.gridLayout_2.addWidget(self.BunButton, 1, 2, 1, 1)
        self.SmartstoreButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.SmartstoreButton.setObjectName("SmartstoreButton")
        self.gridLayout_2.addWidget(self.SmartstoreButton, 1, 3, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.tab)
        self.label_17.setGeometry(QtCore.QRect(60, 40, 51, 20))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tab)
        self.label_18.setGeometry(QtCore.QRect(45, 80, 71, 20))
        self.label_18.setObjectName("label_18")
        self.MIDEdit = QtWidgets.QLineEdit(self.tab)
        self.MIDEdit.setGeometry(QtCore.QRect(120, 40, 341, 20))
        self.MIDEdit.setObjectName("MIDEdit")
        self.MPWEdit = QtWidgets.QLineEdit(self.tab)
        self.MPWEdit.setGeometry(QtCore.QRect(120, 80, 341, 20))
        self.MPWEdit.setObjectName("MPWEdit")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(440, 130, 191, 164))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_3.addWidget(self.label_14)
        self.label_28 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_3.addWidget(self.label_28)
        self.label_29 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_3.addWidget(self.label_29)
        self.label_30 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_3.addWidget(self.label_30)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(40, 20, 571, 86))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_37 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_37.setObjectName("label_37")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_37)
        self.PEEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.PEEdit.setObjectName("PEEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.PEEdit)
        self.label_38 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_38.setObjectName("label_38")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_38)
        self.label_39 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_39.setObjectName("label_39")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_39)
        self.PEPWEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.PEPWEdit.setObjectName("PEPWEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.PEPWEdit)
        self.PEIDEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.PEIDEdit.setObjectName("PEIDEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.PEIDEdit)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(40, 130, 511, 188))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.HSDButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.HSDButton.setObjectName("HSDButton")
        self.gridLayout_3.addWidget(self.HSDButton, 3, 0, 1, 1)
        self.ASDButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.ASDButton.setObjectName("ASDButton")
        self.gridLayout_3.addWidget(self.ASDButton, 1, 0, 1, 1)
        self.ISDButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.ISDButton.setObjectName("ISDButton")
        self.gridLayout_3.addWidget(self.ISDButton, 2, 0, 1, 1)
        self.NSDButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.NSDButton.setObjectName("NSDButton")
        self.gridLayout_3.addWidget(self.NSDButton, 4, 0, 1, 1)
        self.GSSButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.GSSButton.setObjectName("GSSButton")
        self.gridLayout_3.addWidget(self.GSSButton, 0, 1, 1, 1)
        self.GSBButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.GSBButton.setObjectName("GSBButton")
        self.gridLayout_3.addWidget(self.GSBButton, 0, 2, 1, 1)
        self.ASSButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.ASSButton.setObjectName("ASSButton")
        self.gridLayout_3.addWidget(self.ASSButton, 1, 1, 1, 1)
        self.ISSButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.ISSButton.setObjectName("ISSButton")
        self.gridLayout_3.addWidget(self.ISSButton, 2, 1, 1, 1)
        self.ISBButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.ISBButton.setObjectName("ISBButton")
        self.gridLayout_3.addWidget(self.ISBButton, 2, 2, 1, 1)
        self.HSSButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.HSSButton.setObjectName("HSSButton")
        self.gridLayout_3.addWidget(self.HSSButton, 3, 1, 1, 1)
        self.ASBButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.ASBButton.setObjectName("ASBButton")
        self.gridLayout_3.addWidget(self.ASBButton, 1, 2, 1, 1)
        self.NSSButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.NSSButton.setObjectName("NSSButton")
        self.gridLayout_3.addWidget(self.NSSButton, 4, 1, 1, 1)
        self.NSBButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.NSBButton.setObjectName("NSBButton")
        self.gridLayout_3.addWidget(self.NSBButton, 4, 2, 1, 1)
        self.HSBButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.HSBButton.setObjectName("HSBButton")
        self.gridLayout_3.addWidget(self.HSBButton, 3, 2, 1, 1)
        self.GSDButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.GSDButton.setObjectName("GSDButton")
        self.gridLayout_3.addWidget(self.GSDButton, 0, 0, 1, 1)
        self.KSDButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.KSDButton.setObjectName("KSDButton")
        self.gridLayout_3.addWidget(self.KSDButton, 5, 0, 1, 1)
        self.KSSButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.KSSButton.setObjectName("KSSButton")
        self.gridLayout_3.addWidget(self.KSSButton, 5, 1, 1, 1)
        self.KSBButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.KSBButton.setObjectName("KSBButton")
        self.gridLayout_3.addWidget(self.KSBButton, 5, 2, 1, 1)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(600, 130, 221, 191))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_31 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_4.addWidget(self.label_31)
        self.label_33 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_33.setObjectName("label_33")
        self.verticalLayout_4.addWidget(self.label_33)
        self.label_34 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_4.addWidget(self.label_34)
        self.label_36 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_36.setObjectName("label_36")
        self.verticalLayout_4.addWidget(self.label_36)
        self.label_32 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_4.addWidget(self.label_32)
        self.label_35 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_4.addWidget(self.label_35)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ShoppingCombo.setItemText(0, _translate("MainWindow", "쇼핑몰전체"))
        self.ShoppingCombo.setItemText(1, _translate("MainWindow", "옥션"))
        self.ShoppingCombo.setItemText(2, _translate("MainWindow", "지마켓"))
        self.ShoppingCombo.setItemText(3, _translate("MainWindow", "인터파크-B"))
        self.ShoppingCombo.setItemText(4, _translate("MainWindow", "인터파크"))
        self.ShoppingCombo.setItemText(5, _translate("MainWindow", "스마트스토어"))
        self.ShoppingCombo.setItemText(6, _translate("MainWindow", "11번가"))
        self.ShoppingCombo.setItemText(7, _translate("MainWindow", "쿠팡"))
        self.ShoppingCombo.setItemText(8, _translate("MainWindow", "NH마켓"))
        self.ShoppingCombo.setItemText(9, _translate("MainWindow", "카카오톡 스토어"))
        self.ShoppingCombo.setItemText(10, _translate("MainWindow", "위메프2.0"))
        self.ShoppingCombo.setItemText(11, _translate("MainWindow", "티몬(오픈마켓)"))
        self.label_41.setText(_translate("MainWindow", "아이디"))
        self.label_42.setText(_translate("MainWindow", "비밀번호"))
        self.RegisterCombo.setItemText(0, _translate("MainWindow", "계정전체"))
        self.RegisterCombo.setItemText(1, _translate("MainWindow", "SDF"))
        self.RegisterCombo.setItemText(2, _translate("MainWindow", "WIZ"))
        self.RegisterCombo.setItemText(3, _translate("MainWindow", "DRT"))
        self.RegisterCombo.setItemText(4, _translate("MainWindow", "DRE"))
        self.RegisterCombo.setItemText(5, _translate("MainWindow", "BAN"))
        self.RegisterCombo.setItemText(6, _translate("MainWindow", "SAL"))
        self.RegisterCombo.setItemText(7, _translate("MainWindow", "SEL"))
        self.DeliveryCombo.setItemText(0, _translate("MainWindow", "배송처 전체"))
        self.DeliveryCombo.setItemText(1, _translate("MainWindow", "DO"))
        self.DeliveryCombo.setItemText(2, _translate("MainWindow", "DO_XTS"))
        self.DeliveryCombo.setItemText(3, _translate("MainWindow", "FD_002"))
        self.DeliveryCombo.setItemText(4, _translate("MainWindow", "FD_025"))
        self.DeliveryCombo.setItemText(5, _translate("MainWindow", "FR"))
        self.DeliveryCombo.setItemText(6, _translate("MainWindow", "ON"))
        self.DeliveryCombo.setItemText(7, _translate("MainWindow", "SU"))
        self.comboBox.setItemText(0, _translate("MainWindow", "japastoremaster7@gmail.com"))
        self.comboBox.setItemText(1, _translate("MainWindow", "wizgardenmaster@gmail.com"))
        self.comboBox.setItemText(2, _translate("MainWindow", "banyhousemaster@gmail.com"))
        self.comboBox.setItemText(3, _translate("MainWindow", "gtcometruemaster@gmail.com"))
        self.comboBox.setItemText(4, _translate("MainWindow", "dolcevitamaster7@gmail.com"))
        self.comboBox.setItemText(5, _translate("MainWindow", "salefikoreamaster@gmail.com"))
        self.comboBox.setItemText(6, _translate("MainWindow", "sodamfoodmaster@gmail.com"))
        self.comboBox.setItemText(7, _translate("MainWindow", "sellallmaster@gmail.com"))
        self.comboBox.setItemText(8, _translate("MainWindow", "yoonhsryan@gmail.com"))
        self.comboBox.setItemText(9, _translate("MainWindow", "dorothymaster7@gmail.com"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "akdntmzlqhem1@"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "!ghkd02161230"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "galaxyedge6+"))
        self.StateCombo.setItemText(0, _translate("MainWindow", "상품상태 전체"))
        self.StateCombo.setItemText(1, _translate("MainWindow", "판매대기"))
        self.StateCombo.setItemText(2, _translate("MainWindow", "승인대기"))
        self.StateCombo.setItemText(3, _translate("MainWindow", "반려"))
        self.StateCombo.setItemText(4, _translate("MainWindow", "판매중"))
        self.StateCombo.setItemText(5, _translate("MainWindow", "종료대기"))
        self.StateCombo.setItemText(6, _translate("MainWindow", "수정대기"))
        self.StateCombo.setItemText(7, _translate("MainWindow", "판매중지"))
        self.StateCombo.setItemText(8, _translate("MainWindow", "일시품절"))
        self.NumberCombo.setItemText(0, _translate("MainWindow", "상품등록개수"))
        self.NumberCombo.setItemText(1, _translate("MainWindow", "10건"))
        self.NumberCombo.setItemText(2, _translate("MainWindow", "25건"))
        self.NumberCombo.setItemText(3, _translate("MainWindow", "50건"))
        self.NumberCombo.setItemText(4, _translate("MainWindow", "100건"))
        self.NumberCombo.setItemText(5, _translate("MainWindow", "300건"))
        self.NumberCombo.setItemText(6, _translate("MainWindow", "500건"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "플레이오토2"))
        self.OKButton.setText(_translate("MainWindow", "확인"))
        self.OKButton.clicked.connect(self.OK)
        self.GE2Button.setText(_translate("MainWindow", "GE2"))
        self.GE2Button.clicked.connect(self.GE2)
        self.GE1Button.setText(_translate("MainWindow", "GE1"))
        self.GE1Button.clicked.connect(self.GE1)
        self.AE2Button.setText(_translate("MainWindow", "AE2"))
        self.AE2Button.clicked.connect(self.AE2)
        self.AE1Button.setText(_translate("MainWindow", "AE1"))
        self.AE1Button.clicked.connect(self.AE1)
        self.label.setText(_translate("MainWindow", "AE1 : 옥션 ESM 판매가능"))
        self.label_2.setText(_translate("MainWindow", "AE2: 옥션 ESM 판매중지"))
        self.label_13.setText(_translate("MainWindow", "GE1 : G마켓 ESM 판매가능"))
        self.label_14.setText(_translate("MainWindow", "GE2 : G마켓 ESM 판매중지"))
        self.label_15.setText(_translate("MainWindow", "DDS : 도로시 주문확정"))
        self.label_16.setText(_translate("MainWindow", "DSS  : 세일파이 주문확정"))
        self.label_19.setText(_translate("MainWindow", "DDP : 도매토피아 원가"))
        self.DBSButton.setText(_translate("MainWindow", "DBS"))
        self.DBSButton.clicked.connect(self.DBS)
        self.DDSButton.setText(_translate("MainWindow", "DDS"))
        self.DDSButton.clicked.connect(self.DDS)
        self.DSSButton.setText(_translate("MainWindow", "DSS"))
        self.DSSButton.clicked.connect(self.DSS)
        self.DPRICEButton.setText(_translate("MainWindow", "DDP"))
        self.DPRICEButton.clicked.connect(self.DDP)
        self.label_20.setText(_translate("MainWindow", "엑셀경로 :"))
        self.label_26.setText(_translate("MainWindow", "DBS : 바나하우스 주문확정"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "도매토피아"))
        self.PANButton.setText(_translate("MainWindow", "시작하기"))
        self.PANButton.clicked.connect(self.PAN)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "플레이오토 상품수"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "마켓 상품삭제"))
        self.label_28.setText(_translate("MainWindow", "NHM : NH마켓 상품삭제"))
        self.label_29.setText(_translate("MainWindow", "IPM : 인터파크 상품삭제"))
        self.label_30.setText(_translate("MainWindow", "SSM : 스마트스포어 상품삭제"))
        self.NHButton.setText(_translate("MainWindow", "NHM"))
        self.NHButton.clicked.connect(self.NHM)
        self.InterparkButton.setText(_translate("MainWindow", "IPM"))
        self.BunButton.setText(_translate("MainWindow", "BBM"))
        self.SmartstoreButton.setText(_translate("MainWindow", "SSM"))
        self.label_17.setText(_translate("MainWindow", "아이디: "))
        self.label_18.setText(_translate("MainWindow", "비밀번호:"))
        self.label_31.setText(_translate("MainWindow", "GSB : G마켓 엑셀선택"))
        self.label_32.setText(_translate("MainWindow", "ASB : 옥션 엑셀선택"))
        self.label_33.setText(_translate("MainWindow", "ISB  : 인터파크 엑셀선택"))
        self.label_34.setText(_translate("MainWindow", "HSB : NH마켓 엑셀선택"))
        self.label_35.setText(_translate("MainWindow", "NSB : 네이버 엑셀선택"))
        self.label_36.setText(_translate("MainWindow", "KSB : 11번가 엑셀선택"))
        self.HSDButton.setText(_translate("MainWindow", "HSD"))
        self.HSDButton.clicked.connect(self.HSD)
        self.ASDButton.setText(_translate("MainWindow", "ASD"))
        self.ASDButton.clicked.connect(self.ASD)
        self.ISDButton.setText(_translate("MainWindow", "ISD"))
        self.ISDButton.clicked.connect(self.ISD)
        self.NSDButton.setText(_translate("MainWindow", "NSD"))
        self.NSDButton.clicked.connect(self.NSD)
        self.GSSButton.setText(_translate("MainWindow", "GSS"))
        self.GSSButton.clicked.connect(self.GSS)
        self.GSBButton.setText(_translate("MainWindow", "GSB"))
        self.GSBButton.clicked.connect(self.GSB)
        self.ASSButton.setText(_translate("MainWindow", "ASS"))
        self.ASSButton.clicked.connect(self.ASS)
        self.ISSButton.setText(_translate("MainWindow", "ISS"))
        self.ISSButton.clicked.connect(self.ISS)
        self.ISBButton.setText(_translate("MainWindow", "ISB"))
        self.ISBButton.clicked.connect(self.ISB)
        self.HSSButton.setText(_translate("MainWindow", "HSS"))
        self.HSSButton.clicked.connect(self.HSS)
        self.ASBButton.setText(_translate("MainWindow", "ASB"))
        self.ASBButton.clicked.connect(self.ASB)
        self.NSSButton.setText(_translate("MainWindow", "NSS"))
        self.NSSButton.clicked.connect(self.NSS)
        self.NSBButton.setText(_translate("MainWindow", "NSB"))
        self.NSBButton.clicked.connect(self.NSB)
        self.HSBButton.setText(_translate("MainWindow", "HSB"))
        self.HSBButton.clicked.connect(self.HSB)
        self.GSDButton.setText(_translate("MainWindow", "GSD"))
        self.GSDButton.clicked.connect(self.GSD)
        self.KSDButton.setText(_translate("MainWindow", "KSD"))
        self.KSDButton.clicked.connect(self.KSD)
        self.KSSButton.setText(_translate("MainWindow", "KSS"))
        self.KSSButton.clicked.connect(self.KSS)
        self.KSBButton.setText(_translate("MainWindow", "KSB"))
        self.KSBButton.clicked.connect(self.KSB)
        self.label_37.setText(_translate("MainWindow", "엑셀경로"))
        self.label_38.setText(_translate("MainWindow", "비밀번호"))
        self.label_39.setText(_translate("MainWindow", "아이디"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "도매토피아 엑셀"))
    
    def OK(self):
        id=self.comboBox.currentText()
        pw=self.comboBox_2.currentText()
        while(1):
            try:
                driver.get('https://app.playauto.io/login.html')
                time.sleep(2)
                driver.find_element_by_name("email").send_keys(id)
                driver.find_element_by_name("password").send_keys(pw)
                driver.find_element_by_xpath('/html/body/div[3]/div/div/form/div/div[5]/div/button').click()
                time.sleep(5)
                break
            except:
                driver.find_element_by_xpath('/html/body/div[5]/div[7]/div/button').click()
                driver.refresh()
                break
        shopping=self.ShoppingCombo.currentIndex()
        register=self.RegisterCombo.currentText()
        delivery=self.DeliveryCombo.currentIndex()
        state=self.StateCombo.currentIndex()
        numbering=self.NumberCombo.currentIndex()

        j=1
        while(1):
            try:
                driver.get('https://app.playauto.io/#!/online/product/list')
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="search-detail-shop_cd"]/option['+str(int(shopping)+1)+']').click()
                driver.find_element_by_xpath('//*[@id="search-detail-sale_status"]/option['+str(int(state)+1)+']').click()
                driver.find_element_by_xpath('//*[@id="search-detail-depot_no"]/option['+str(int(delivery)+1)+']').click()
                html=driver.page_source
                soup=BeautifulSoup(html,'html.parser')
                for i in soup.select('#search-detail-shop_id > option'):
                    if register in i.text:
                        driver.find_element_by_xpath('//*[@id="search-detail-shop_id"]/option['+str(j)+']').click()
                    j+=1
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[2]/div[1]/div/div/button').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div[1]/div[2]/div[1]/div[3]/div[1]/select/option['+str(int(numbering))+']').click()
                if int(shopping)+1==2 or int(shopping)+1==3 or int(shopping)+1==7:     ##일반,단일상품선택
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div[1]/div[1]/ul/li[3]/a').click()
                    time.sleep(2)
                    while(1):
                        try:
                            if int(state)+1==2 or int(state)+1==7:##판매대기,수정대기->상품전송
                                driver.find_element_by_css_selector('div.ui-grid-header > div > div > div > div > div > div.ui-grid-header-cell.ui-grid-clearfix.ui-grid-coluiGrid-0005 > div > div > div').click()
                                time.sleep(2)
                                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div[1]/div[2]/div[1]/div[2]/div[3]/button').click()
                                time.sleep(2)
                                driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                                time.sleep(10)
                                driver.find_element_by_xpath('//*[@id="shop_product_grid"]/div/div[2]/div[1]/div[1]/button[3]').click()
                                time.sleep(5)
                            else:#판매중->연동해제
                                driver.find_element_by_css_selector('div.ui-grid-header > div > div > div > div > div > div.ui-grid-header-cell.ui-grid-clearfix.ui-grid-coluiGrid-0005 > div > div > div').click()
                                time.sleep(2)
                                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div[1]/div[2]/div[1]/div[2]/div[10]/button').click()
                                time.sleep(2)
                                driver.find_element_by_xpath('//*[@id="prod_linkage_modify"]/div/div[3]/button[1]').click()
                                time.sleep(10)
                                driver.find_element_by_xpath('//*[@id="shop_product_grid"]/div/div[2]/div[1]/div[1]/button[3]').click()
                                time.sleep(5)
                        except:
                            print("전송오류")
                            break
                else:
                    time.sleep(2)
                    while(1):
                        try:
                            if int(state)+1==2 or int(state)+1==7:
                                driver.find_element_by_css_selector('div.ui-grid-header > div > div > div > div > div > div.ui-grid-header-cell.ui-grid-clearfix.ui-grid-coluiGrid-0005 > div > div > div').click()
                                time.sleep(2)
                                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div[1]/div[2]/div[1]/div[2]/div[3]/button').click()
                                time.sleep(2)
                                driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                                time.sleep(10)
                                driver.find_element_by_xpath('//*[@id="shop_product_grid"]/div/div[2]/div[1]/div[1]/button[3]').click()
                                time.sleep(5)
                            else:
                                driver.find_element_by_css_selector('div.ui-grid-header > div > div > div > div > div > div.ui-grid-header-cell.ui-grid-clearfix.ui-grid-coluiGrid-0005 > div > div > div').click()
                                time.sleep(2)
                                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div[1]/div[2]/div[1]/div[2]/div[10]/button').click()
                                time.sleep(2)
                                driver.find_element_by_xpath('//*[@id="prod_linkage_modify"]/div/div[3]/button[1]').click()
                                time.sleep(10)
                                driver.find_element_by_xpath('//*[@id="shop_product_grid"]/div/div[2]/div[1]/div[1]/button[3]').click()
                                time.sleep(5)
                        except:
                            print("전송오류")
                            break
                html=driver.page_source
                soup=BeautifulSoup(html,'html.parser')
                for k in soup.select('body > ui-view > div.page-container > div > div.content-wrapper.content-wrapper-main > div:nth-child(3) > div > div > div.a-content > div.a-content-nav-tabs-box > ul > li:nth-child(1) > a > span'):
                    print(k.string)
                    if int(k.string)>0:
                        print("남아있다")
                        driver.get('https://app.playauto.io/#!/home')
                        continue
                    else:
                        return True
            except:
                driver.refresh()
                print("재시작")
                j=1
                continue

    def KSB(self):
        i=1
        excel=win32com.client.Dispatch("Excel.Application")
        excel.Visible=True
        url=self.PEEdit.text()
        wb=excel.workbooks.Open(url)
        ws=wb.ActiveSheet

        id=self.PEIDEdit.text()
        pw=self.PEPWEdit.text()
        driver.get('https://app.playauto.io/login.html')
        time.sleep(2)
        driver.find_element_by_name("email").send_keys(id)
        driver.find_element_by_name("password").send_keys(pw)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/form/div/div[5]/div/button').click()
        time.sleep(5)

        while(1):
            driver.get('https://app.playauto.io/#!/online/product/list')
            time.sleep(5)
            driver.refresh()
            time.sleep(5)
            while(1):
                try:
                    code=ws.Cells(i,1).Value
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(code)
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(Keys.ENTER)
                    i+=1
                    if ws.Cells(i,1).Value==None:
                        break
                except:
                    driver.refresh()
                    i=1
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[2]/div[1]/div/div/button').click()
            try:
                driver.find_element_by_xpath('//*[@id="online_product_grid_searchbar"]/div/ul/li[2]/a').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[7]/treeitem/ul/li[2]/i[1]').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[7]/treeitem/ul/li[2]/treeitem/ul/li[1]/div').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[3]/a').click()
            except:
                print("retry")
                driver.refresh()
                time.sleep(5)
                continue
            while(1):
                try:
                    time.sleep(5)
                    driver.find_element_by_css_selector('div.ui-grid-header > div > div > div > div > div > div.ui-grid-header-cell.ui-grid-clearfix.ui-grid-coluiGrid-0005 > div > div > div').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                    time.sleep(10)
                    try:
                        driver.find_element_by_xpath('//*[@id="shop_product_grid"]/div/div[2]/div[1]/div[1]/button[3]').click()
                    except:
                        break
                except:
                    break
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(3) > a > span'):
                print(j.string)
                if int(j.string)>0:
                    print("남아있다")
                    driver.get('https://app.playauto.io/#!/home')
                    break
                else:
                    return True


    def KSS(self):
        i=1
        excel=win32com.client.Dispatch("Excel.Application")
        excel.Visible=True
        url=self.PEEdit.text()
        wb=excel.workbooks.Open(url)
        ws=wb.ActiveSheet

        id=self.PEIDEdit.text()
        pw=self.PEPWEdit.text()
        driver.get('https://app.playauto.io/login.html')
        time.sleep(2)
        driver.find_element_by_name("email").send_keys(id)
        driver.find_element_by_name("password").send_keys(pw)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/form/div/div[5]/div/button').click()
        time.sleep(5)

        while(1):
            driver.get('https://app.playauto.io/#!/online/product/list')
            time.sleep(5)
            driver.refresh()
            time.sleep(5)
            while(1):
                try:
                    code=ws.Cells(i,1).Value
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(code)
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(Keys.ENTER)
                    i+=1
                    if ws.Cells(i,1).Value==None:
                        break
                except:
                    driver.refresh()
                    i=1
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[2]/div[1]/div/div/button').click()
            try:
                driver.find_element_by_xpath('//*[@id="online_product_grid_searchbar"]/div/ul/li[2]/a').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[7]/treeitem/ul/li[4]/i[1]').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[7]/treeitem/ul/li[4]/treeitem/ul/li[1]/div').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[3]/a').click()
            except:
                print("retry")
                driver.refresh()
                continue
            while(1):
                try:
                    time.sleep(5)
                    driver.find_element_by_css_selector('div.ui-grid-header > div > div > div > div > div > div.ui-grid-header-cell.ui-grid-clearfix.ui-grid-coluiGrid-0005 > div > div > div').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                    time.sleep(10)
                    driver.find_element_by_xpath('//*[@id="shop_product_grid"]/div/div[2]/div[1]/div[1]/button[3]').click()
                    time.sleep(5)
                except:
                    break
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(3) > a > span'):
                print(j.string)
                if int(j.string)>0:
                    print("남아있다")
                    driver.get('https://app.playauto.io/#!/home')
                    break
                else:
                    return True

    
    def KSD(self):
        i=1
        excel=win32com.client.Dispatch("Excel.Application")
        excel.Visible=True
        url=self.PEEdit.text()
        wb=excel.workbooks.Open(url)
        ws=wb.ActiveSheet

        id=self.PEIDEdit.text()
        pw=self.PEPWEdit.text()
        driver.get('https://app.playauto.io/login.html')
        time.sleep(2)
        driver.find_element_by_name("email").send_keys(id)
        driver.find_element_by_name("password").send_keys(pw)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/form/div/div[5]/div/button').click()
        time.sleep(5)

        while(1):
            driver.get('https://app.playauto.io/#!/online/product/list')
            time.sleep(5)
            driver.refresh()
            time.sleep(5)
            while(1):
                try:
                    code=ws.Cells(i,1).Value
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(code)
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(Keys.ENTER)
                    i+=1
                    if ws.Cells(i,1).Value==None:
                        break
                except:
                    driver.refresh()
                    i=1
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[2]/div[1]/div/div/button').click()
            try:
                driver.find_element_by_xpath('//*[@id="online_product_grid_searchbar"]/div/ul/li[2]/a').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[7]/treeitem/ul/li[5]/i[1]').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[7]/treeitem/ul/li[5]/treeitem/ul/li[1]/div').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[3]/a').click()
            except:
                print("retry")
                driver.refresh()
                time.sleep(5)
                continue
            while(1):
                try:
                    time.sleep(5)
                    driver.find_element_by_css_selector('div.ui-grid-header > div > div > div > div > div > div.ui-grid-header-cell.ui-grid-clearfix.ui-grid-coluiGrid-0005 > div > div > div').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                    time.sleep(10)
                    try:
                        driver.find_element_by_xpath('//*[@id="shop_product_grid"]/div/div[2]/div[1]/div[1]/button[3]').click()
                    except:
                        break
                except:
                    break
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(3) > a > span'):
                print(j.string)
                if int(j.string)>0:
                    print("남아있다")
                    driver.get('https://app.playauto.io/#!/home')
                    break
                else:
                    return True


    def HSB(self):
        i=1
        excel=win32com.client.Dispatch("Excel.Application")
        excel.Visible=True
        url=self.PEEdit.text()
        wb=excel.workbooks.Open(url)
        ws=wb.ActiveSheet

        id=self.PEIDEdit.text()
        pw=self.PEPWEdit.text()
        driver.get('https://app.playauto.io/login.html')
        time.sleep(2)
        driver.find_element_by_name("email").send_keys(id)
        driver.find_element_by_name("password").send_keys(pw)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/form/div/div[5]/div/button').click()
        time.sleep(5)

        while(1):
            i=1
            driver.get('https://app.playauto.io/#!/online/product/list')
            time.sleep(5)
            driver.refresh()
            time.sleep(5)
            while(1):
                try:
                    code=ws.Cells(i,1).Value
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(code)
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(Keys.ENTER)
                    i+=1
                    if ws.Cells(i,1).Value==None:
                        break
                except:
                    driver.refresh()
                    i=1
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[2]/div[1]/div/div/button').click()
            time.sleep(2)
            try:
                driver.find_element_by_xpath('//*[@id="online_product_grid_searchbar"]/div/ul/li[2]/a').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[9]/treeitem/ul/li[2]/i[1]').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[9]/treeitem/ul/li[2]/treeitem/ul/li[1]/div').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[2]/a').click()
            except:
                print("retry")
                driver.refresh()
                continue
            while(1):
                try:
                    time.sleep(5)
                    driver.find_element_by_css_selector('div.ui-grid-header > div > div > div > div > div > div.ui-grid-header-cell.ui-grid-clearfix.ui-grid-coluiGrid-0005 > div > div > div').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                    time.sleep(10)
                    try:
                        driver.find_element_by_xpath('//*[@id="shop_product_grid"]/div/div[2]/div[1]/div[1]/button[3]').click()
                    except:
                         break
                except:
                    break
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(2) > a > span'):
                print(j.string)
                if int(j.string)>0:
                    print("남아있다")
                    driver.get('https://app.playauto.io/#!/home')
                    break
                else:
                    return True


    def HSS(self):
        i=1
        excel=win32com.client.Dispatch("Excel.Application")
        excel.Visible=True
        url=self.PEEdit.text()
        wb=excel.workbooks.Open(url)
        ws=wb.ActiveSheet

        id=self.PEIDEdit.text()
        pw=self.PEPWEdit.text()
        driver.get('https://app.playauto.io/login.html')
        time.sleep(2)
        driver.find_element_by_name("email").send_keys(id)
        driver.find_element_by_name("password").send_keys(pw)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/form/div/div[5]/div/button').click()
        time.sleep(5)

        while(1):
            driver.get('https://app.playauto.io/#!/online/product/list')
            time.sleep(5)
            driver.refresh()
            time.sleep(5)
            while(1):
                try:
                    code=ws.Cells(i,1).Value
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(code)
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(Keys.ENTER)
                    i+=1
                    if ws.Cells(i,1).Value==None:
                        break
                except:
                    driver.refresh()
                    i=1
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[2]/div[1]/div/div/button').click()
            try:
                driver.find_element_by_xpath('//*[@id="online_product_grid_searchbar"]/div/ul/li[2]/a').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[9]/treeitem/ul/li[4]/i[1]').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[9]/treeitem/ul/li[4]/treeitem/ul/li[1]/div').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[2]/a').click()
            except:
                print("retry")
                driver.refresh()
                continue
            while(1):
                try:
                    time.sleep(5)
                    driver.find_element_by_css_selector('div.ui-grid-header > div > div > div > div > div > div.ui-grid-header-cell.ui-grid-clearfix.ui-grid-coluiGrid-0005 > div > div > div').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                    time.sleep(10)
                    try:
                        driver.find_element_by_xpath('//*[@id="shop_product_grid"]/div/div[2]/div[1]/div[1]/button[3]').click()
                    except:
                        break
                except:
                    break
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(2) > a > span'):
                print(j.string)
                if int(j.string)>0:
                    print("남아있다")
                    driver.get('https://app.playauto.io/#!/home')
                    break
                else:
                    return True


    def HSD(self):
        i=1
        excel=win32com.client.Dispatch("Excel.Application")
        excel.Visible=True
        url=self.PEEdit.text()
        wb=excel.workbooks.Open(url)
        ws=wb.ActiveSheet

        id=self.PEIDEdit.text()
        pw=self.PEPWEdit.text()
        driver.get('https://app.playauto.io/login.html')
        time.sleep(2)
        driver.find_element_by_name("email").send_keys(id)
        driver.find_element_by_name("password").send_keys(pw)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/form/div/div[5]/div/button').click()
        time.sleep(5)

        while(1):
            driver.get('https://app.playauto.io/#!/online/product/list')
            time.sleep(5)
            driver.refresh()
            time.sleep(5)
            while(1):
                try:
                    code=ws.Cells(i,1).Value
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(code)
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(Keys.ENTER)
                    i+=1
                    if ws.Cells(i,1).Value==None:
                        break
                except:
                    driver.refresh()
                    i=1
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[2]/div[1]/div/div/button').click()
            try:
                driver.find_element_by_xpath('//*[@id="online_product_grid_searchbar"]/div/ul/li[2]/a').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[9]/treeitem/ul/li[3]/i[1]').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[9]/treeitem/ul/li[3]/treeitem/ul/li[1]/div').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[2]/a').click()
            except:
                print("retry")
                driver.refresh()
                continue
            while(1):
                try:
                    time.sleep(5)
                    driver.find_element_by_css_selector('div.ui-grid-header > div > div > div > div > div > div.ui-grid-header-cell.ui-grid-clearfix.ui-grid-coluiGrid-0005 > div > div > div').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                    time.sleep(10)
                    try:
                        driver.find_element_by_xpath('//*[@id="shop_product_grid"]/div/div[2]/div[1]/div[1]/button[3]').click()
                    except:
                         break
                except:
                    break
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(2) > a > span'):
                print(j.string)
                if int(j.string)>0:
                    print("남아있다")
                    driver.get('https://app.playauto.io/#!/home')
                    break
                else:
                    return True


    def NSB(self):
        i=1
        excel=win32com.client.Dispatch("Excel.Application")
        excel.Visible=True
        url=self.PEEdit.text()
        wb=excel.workbooks.Open(url)
        ws=wb.ActiveSheet

        id=self.PEIDEdit.text()
        pw=self.PEPWEdit.text()
        driver.get('https://app.playauto.io/login.html')
        time.sleep(2)
        driver.find_element_by_name("email").send_keys(id)
        driver.find_element_by_name("password").send_keys(pw)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/form/div/div[5]/div/button').click()
        time.sleep(5)

        while(1):
            driver.get('https://app.playauto.io/#!/online/product/list')
            time.sleep(5)
            driver.refresh()
            time.sleep(5)
            while(1):
                try:
                    code=ws.Cells(i,1).Value
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(code)
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(Keys.ENTER)
                    i+=1
                    if ws.Cells(i,1).Value==None:
                        break
                except:
                    driver.refresh()
                    i=1
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[2]/div[1]/div/div/button').click()
            try:
                driver.find_element_by_xpath('//*[@id="online_product_grid_searchbar"]/div/ul/li[2]/a').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[6]/treeitem/ul/li[3]/i[1]').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[6]/treeitem/ul/li[3]/treeitem/ul/li[1]/div').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[2]/a').click()
            except:
                print("retry")
                driver.refresh()
                continue
            while(1):
                try:
                    time.sleep(5)
                    driver.find_element_by_css_selector('div.ui-grid-header > div > div > div > div > div > div.ui-grid-header-cell.ui-grid-clearfix.ui-grid-coluiGrid-0005 > div > div > div').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                    time.sleep(10)
                    try:
                        driver.find_element_by_xpath('//*[@id="shop_product_grid"]/div/div[2]/div[1]/div[1]/button[3]').click()
                    except:
                        break
                except:
                    break
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(2) > a > span'):
                print(j.string)
                if int(j.string)>0:
                    print("남아있다")
                    driver.get('https://app.playauto.io/#!/home')
                    break
                else:
                    return True


    def NSS(self):
        i=1
        excel=win32com.client.Dispatch("Excel.Application")
        excel.Visible=True
        url=self.PEEdit.text()
        wb=excel.workbooks.Open(url)
        ws=wb.ActiveSheet

        id=self.PEIDEdit.text()
        pw=self.PEPWEdit.text()
        driver.get('https://app.playauto.io/login.html')
        time.sleep(2)
        driver.find_element_by_name("email").send_keys(id)
        driver.find_element_by_name("password").send_keys(pw)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/form/div/div[5]/div/button').click()
        time.sleep(5)

        while(1):
            driver.get('https://app.playauto.io/#!/online/product/list')
            time.sleep(5)
            driver.refresh()
            time.sleep(5)
            while(1):
                try:
                    code=ws.Cells(i,1).Value
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(code)
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(Keys.ENTER)
                    i+=1
                    if ws.Cells(i,1).Value==None:
                        break
                except:
                    driver.refresh()
                    i=1
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[2]/div[1]/div/div/button').click()
            try:
                driver.find_element_by_xpath('//*[@id="online_product_grid_searchbar"]/div/ul/li[2]/a').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[6]/treeitem/ul/li[5]/i[1]').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[6]/treeitem/ul/li[5]/treeitem/ul/li[1]/div').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[2]/a').click()
            except:
                print("retry")
                driver.refresh()
                continue
            while(1):
                try:
                    time.sleep(5)
                    driver.find_element_by_css_selector('div.ui-grid-header > div > div > div > div > div > div.ui-grid-header-cell.ui-grid-clearfix.ui-grid-coluiGrid-0005 > div > div > div').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                    time.sleep(10)
                    try:
                        driver.find_element_by_xpath('//*[@id="shop_product_grid"]/div/div[2]/div[1]/div[1]/button[3]').click()
                    except:
                        break
                except:
                    break
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(2) > a > span'):
                print(j.string)
                if int(j.string)>0:
                    print("남아있다")
                    driver.get('https://app.playauto.io/#!/home')
                    break
                else:
                    return True


    def NSD(self):
        i=1
        excel=win32com.client.Dispatch("Excel.Application")
        excel.Visible=True
        url=self.PEEdit.text()
        wb=excel.workbooks.Open(url)
        ws=wb.ActiveSheet

        id=self.PEIDEdit.text()
        pw=self.PEPWEdit.text()
        driver.get('https://app.playauto.io/login.html')
        time.sleep(2)
        driver.find_element_by_name("email").send_keys(id)
        driver.find_element_by_name("password").send_keys(pw)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/form/div/div[5]/div/button').click()
        time.sleep(5)

        while(1):
            driver.get('https://app.playauto.io/#!/online/product/list')
            time.sleep(5)
            driver.refresh()
            time.sleep(5)
            while(1):
                try:
                    code=ws.Cells(i,1).Value
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(code)
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(Keys.ENTER)
                    i+=1
                    if ws.Cells(i,1).Value==None:
                        break
                except:
                    driver.refresh()
                    i=1
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[2]/div[1]/div/div/button').click()
            try:
                driver.find_element_by_xpath('//*[@id="online_product_grid_searchbar"]/div/ul/li[2]/a').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[6]/treeitem/ul/li[6]/i[1]').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[6]/treeitem/ul/li[6]/treeitem/ul/li[1]/div').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[2]/a').click()
            except:
                print("retry")
                driver.refresh()
                continue
            while(1):
                try:
                    time.sleep(5)
                    driver.find_element_by_css_selector('div.ui-grid-header > div > div > div > div > div > div.ui-grid-header-cell.ui-grid-clearfix.ui-grid-coluiGrid-0005 > div > div > div').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                    time.sleep(10)
                    try:
                        driver.find_element_by_xpath('//*[@id="shop_product_grid"]/div/div[2]/div[1]/div[1]/button[3]').click()
                    except:
                        break
                except:
                    break
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(2) > a > span'):
                print(j.string)
                if int(j.string)>0:
                    print("남아있다")
                    driver.get('https://app.playauto.io/#!/home')
                    break
                else:
                    return True


    def ISB(self):
        i=1
        excel=win32com.client.Dispatch("Excel.Application")
        excel.Visible=True
        url=self.PEEdit.text()
        wb=excel.workbooks.Open(url)
        ws=wb.ActiveSheet

        id=self.PEIDEdit.text()
        pw=self.PEPWEdit.text()
        driver.get('https://app.playauto.io/login.html')
        time.sleep(2)
        driver.find_element_by_name("email").send_keys(id)
        driver.find_element_by_name("password").send_keys(pw)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/form/div/div[5]/div/button').click()
        time.sleep(5)

        while(1):
            driver.get('https://app.playauto.io/#!/online/product/list')
            time.sleep(5)
            driver.refresh()
            time.sleep(5)
            while(1):
                try:
                    code=ws.Cells(i,1).Value
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(code)
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(Keys.ENTER)
                    i+=1
                    if ws.Cells(i,1).Value==None:
                        break
                except:
                    driver.refresh()
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[2]/div[1]/div/div/button').click()
            try:
                driver.find_element_by_xpath('//*[@id="online_product_grid_searchbar"]/div/ul/li[2]/a').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[5]/treeitem/ul/li[2]/i[1]').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[5]/treeitem/ul/li[2]/treeitem/ul/li[1]/div').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[2]/a').click()
            except:
                print("retry")
                driver.refresh()
                continue
            while(1):
                try:
                    time.sleep(5)
                    driver.find_element_by_css_selector('div.ui-grid-header > div > div > div > div > div > div.ui-grid-header-cell.ui-grid-clearfix.ui-grid-coluiGrid-0005 > div > div > div').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                    time.sleep(10)
                    try:
                        driver.find_element_by_xpath('//*[@id="shop_product_grid"]/div/div[2]/div[1]/div[1]/button[3]').click()
                    except:
                        break
                except:
                    break
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(2) > a > span'):
                print(j.string)
                if int(j.string)>0:
                    print("남아있다")
                    driver.get('https://app.playauto.io/#!/home')
                    break
                else:
                    return True


    def ISS(self):
        i=1
        excel=win32com.client.Dispatch("Excel.Application")
        excel.Visible=True
        url=self.PEEdit.text()
        wb=excel.workbooks.Open(url)
        ws=wb.ActiveSheet

        id=self.PEIDEdit.text()
        pw=self.PEPWEdit.text()
        driver.get('https://app.playauto.io/login.html')
        time.sleep(2)
        driver.find_element_by_name("email").send_keys(id)
        driver.find_element_by_name("password").send_keys(pw)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/form/div/div[5]/div/button').click()
        time.sleep(5)

        while(1):
            driver.get('https://app.playauto.io/#!/online/product/list')
            time.sleep(5)
            driver.refresh()
            time.sleep(5)
            while(1):
                try:
                    code=ws.Cells(i,1).Value
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(code)
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(Keys.ENTER)
                    i+=1
                    if ws.Cells(i,1).Value==None:
                        break
                except:
                    driver.refresh()
                    i=1
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[2]/div[1]/div/div/button').click()
            try:
                driver.find_element_by_xpath('//*[@id="online_product_grid_searchbar"]/div/ul/li[2]/a').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[5]/treeitem/ul/li[3]/i[1]').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[5]/treeitem/ul/li[3]/treeitem/ul/li[1]/div').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[2]/a').click()
            except:
                print("retry")
                driver.refresh()
                continue
            while(1):
                try:
                    time.sleep(5)
                    driver.find_element_by_css_selector('div.ui-grid-header > div > div > div > div > div > div.ui-grid-header-cell.ui-grid-clearfix.ui-grid-coluiGrid-0005 > div > div > div').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                    time.sleep(10)
                    try:
                        driver.find_element_by_xpath('//*[@id="shop_product_grid"]/div/div[2]/div[1]/div[1]/button[3]').click()
                    except:
                        break
                except:
                    break
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(2) > a > span'):
                print(j.string)
                if int(j.string)>0:
                    print("남아있다")
                    driver.get('https://app.playauto.io/#!/home')
                    break
                else:
                    return True


    def ISD(self):
        i=1
        excel=win32com.client.Dispatch("Excel.Application")
        excel.Visible=True
        url=self.PEEdit.text()
        wb=excel.workbooks.Open(url)
        ws=wb.ActiveSheet

        id=self.PEIDEdit.text()
        pw=self.PEPWEdit.text()
        driver.get('https://app.playauto.io/login.html')
        time.sleep(2)
        driver.find_element_by_name("email").send_keys(id)
        driver.find_element_by_name("password").send_keys(pw)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/form/div/div[5]/div/button').click()
        time.sleep(5)

        while(1):
            driver.get('https://app.playauto.io/#!/online/product/list')
            time.sleep(5)
            driver.refresh()
            time.sleep(5)
            while(1):
                try:
                    code=ws.Cells(i,1).Value
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(code)
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(Keys.ENTER)
                    i+=1
                    if ws.Cells(i,1).Value==None:
                        break
                except:
                    driver.refresh()
                    i=1
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[2]/div[1]/div/div/button').click()
            try:
                driver.find_element_by_xpath('//*[@id="online_product_grid_searchbar"]/div/ul/li[2]/a').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[5]/treeitem/ul/li[4]/i[1]').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[5]/treeitem/ul/li[4]/treeitem/ul/li[1]/div').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[2]/a').click()
            except:
                print("retry")
                driver.refresh()
                continue
            while(1):
                try:
                    time.sleep(5)
                    driver.find_element_by_css_selector('div.ui-grid-header > div > div > div > div > div > div.ui-grid-header-cell.ui-grid-clearfix.ui-grid-coluiGrid-0005 > div > div > div').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                    time.sleep(10)
                    try:
                        driver.find_element_by_xpath('//*[@id="shop_product_grid"]/div/div[2]/div[1]/div[1]/button[3]').click()
                    except:
                        break
                except:
                    break
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(2) > a > span'):
                print(j.string)
                if int(j.string)>0:
                    print("남아있다")
                    driver.get('https://app.playauto.io/#!/home')
                    break
                else:
                    return True


    def ASB(self):
        i=1
        excel=win32com.client.Dispatch("Excel.Application")
        excel.Visible=True
        url=self.PEEdit.text()
        wb=excel.workbooks.Open(url)
        ws=wb.ActiveSheet

        id=self.PEIDEdit.text()
        pw=self.PEPWEdit.text()
        driver.get('https://app.playauto.io/login.html')
        time.sleep(2)
        driver.find_element_by_name("email").send_keys(id)
        driver.find_element_by_name("password").send_keys(pw)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/form/div/div[5]/div/button').click()
        time.sleep(5)

        while(1):
            driver.get('https://app.playauto.io/#!/online/product/list')
            time.sleep(5)
            driver.refresh()
            time.sleep(5)
            while(1):
                try:
                    code=ws.Cells(i,1).Value
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(code)
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(Keys.ENTER)
                    i+=1
                    if ws.Cells(i,1).Value==None:
                        break
                except:
                    driver.refresh()
                    i=1
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[2]/div[1]/div/div/button').click()
            try:
                driver.find_element_by_xpath('//*[@id="online_product_grid_searchbar"]/div/ul/li[2]/a').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[2]/treeitem/ul/li[2]/i[1]').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[2]/treeitem/ul/li[2]/treeitem/ul/li[1]/div').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[3]/a').click()
            except:
                print("retry")
                driver.refresh()
                continue
            while(1):
                try:
                    time.sleep(5)
                    driver.find_element_by_css_selector('div.ui-grid-header > div > div > div > div > div > div.ui-grid-header-cell.ui-grid-clearfix.ui-grid-coluiGrid-0005 > div > div > div').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                    time.sleep(10)
                    try:
                        driver.find_element_by_xpath('//*[@id="shop_product_grid"]/div/div[2]/div[1]/div[1]/button[3]').click()
                    except:
                        break
                except:
                    break
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(3) > a > span'):
                print(j.string)
                if int(j.string)>0:
                    print("남아있다")
                    time.sleep(60)
                    driver.get('https://app.playauto.io/#!/home')
                    break
                else:
                    return True


    def ASS(self):
        i=1
        excel=win32com.client.Dispatch("Excel.Application")
        excel.Visible=True
        url=self.PEEdit.text()
        wb=excel.workbooks.Open(url)
        ws=wb.ActiveSheet

        id=self.PEIDEdit.text()
        pw=self.PEPWEdit.text()
        driver.get('https://app.playauto.io/login.html')
        time.sleep(2)
        driver.find_element_by_name("email").send_keys(id)
        driver.find_element_by_name("password").send_keys(pw)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/form/div/div[5]/div/button').click()
        time.sleep(5)

        while(1):
            driver.get('https://app.playauto.io/#!/online/product/list')
            time.sleep(5)
            driver.refresh()
            time.sleep(5)
            while(1):
                try:
                    code=ws.Cells(i,1).Value
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(code)
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(Keys.ENTER)
                    i+=1
                    if ws.Cells(i,1).Value==None:
                        break
                except:
                    driver.refresh()
                    i=1
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[2]/div[1]/div/div/button').click()
            try:
                driver.find_element_by_xpath('//*[@id="online_product_grid_searchbar"]/div/ul/li[2]/a').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[2]/treeitem/ul/li[4]/i[1]').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[2]/treeitem/ul/li[4]/treeitem/ul/li[1]/div').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[2]/a').click()
            except:
                print("retry")
                driver.refresh()
                continue
            while(1):
                try:
                    time.sleep(5)
                    driver.find_element_by_css_selector('div.ui-grid-header > div > div > div > div > div > div.ui-grid-header-cell.ui-grid-clearfix.ui-grid-coluiGrid-0005 > div > div > div').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                    i=i+1
                    time.sleep(10)
                    try:
                        driver.find_element_by_xpath('//*[@id="shop_product_grid"]/div/div[2]/div[1]/div[1]/button[3]').click()
                    except:
                        break
                except:
                    break
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(3) > a > span'):
                print(j.string)
                if int(j.string)>0:
                    print("남아있다")
                    driver.get('https://app.playauto.io/#!/home')
                    break
                else:
                    return True


    def GSB(self):
        i=1
        excel=win32com.client.Dispatch("Excel.Application")
        excel.Visible=True
        url=self.PEEdit.text()
        wb=excel.workbooks.Open(url)
        ws=wb.ActiveSheet

        id=self.PEIDEdit.text()
        pw=self.PEPWEdit.text()
        driver.get('https://app.playauto.io/login.html')
        time.sleep(2)
        driver.find_element_by_name("email").send_keys(id)
        driver.find_element_by_name("password").send_keys(pw)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/form/div/div[5]/div/button').click()
        time.sleep(5)

        while(1):
            driver.get('https://app.playauto.io/#!/online/product/list')
            time.sleep(5)
            driver.refresh()
            time.sleep(5)
            while(1):
                try:
                    code=ws.Cells(i,1).Value
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(code)
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(Keys.ENTER)
                    i+=1
                    if ws.Cells(i,1).Value==None:
                        break
                except:
                    driver.refresh()
                    i=1
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[2]/div[1]/div/div/button').click()
            try:
                driver.find_element_by_xpath('//*[@id="online_product_grid_searchbar"]/div/ul/li[2]/a').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[3]/treeitem/ul/li[2]/i[1]').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[3]/treeitem/ul/li[2]/treeitem/ul/li[1]/div').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[3]/a').click()
            except:
                print("retry")
                driver.refresh()
                continue
            while(1):
                try:
                    time.sleep(5)
                    driver.find_element_by_css_selector('div.ui-grid-header > div > div > div > div > div > div.ui-grid-header-cell.ui-grid-clearfix.ui-grid-coluiGrid-0005 > div > div > div').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                    time.sleep(10)
                    try:
                        driver.find_element_by_xpath('//*[@id="shop_product_grid"]/div/div[2]/div[1]/div[1]/button[3]').click()
                    except:
                        break
                except:
                    break
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(3) > a > span'):
                print(j.string)
                if int(j.string)>0:
                    print("남아있다")
                    driver.get('https://app.playauto.io/#!/home')
                    break
                else:
                    return True


    def GSS(self):
        i=1
        excel=win32com.client.Dispatch("Excel.Application")
        excel.Visible=True
        url=self.PEEdit.text()
        wb=excel.workbooks.Open(url)
        ws=wb.ActiveSheet

        id=self.PEIDEdit.text()
        pw=self.PEPWEdit.text()
        driver.get('https://app.playauto.io/login.html')
        time.sleep(2)
        driver.find_element_by_name("email").send_keys(id)
        driver.find_element_by_name("password").send_keys(pw)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/form/div/div[5]/div/button').click()
        time.sleep(5)

        while(1):
            driver.get('https://app.playauto.io/#!/online/product/list')
            time.sleep(5)
            driver.refresh()
            time.sleep(5)
            while(1):
                try:
                    code=ws.Cells(i,1).Value
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(code)
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(Keys.ENTER)
                    i+=1
                    if ws.Cells(i,1).Value==None:
                        break
                except:
                    driver.refresh()
                    i=1
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[2]/div[1]/div/div/button').click()
            try:
                driver.find_element_by_xpath('//*[@id="online_product_grid_searchbar"]/div/ul/li[2]/a').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[3]/treeitem/ul/li[4]/i[1]').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[3]/treeitem/ul/li[4]/treeitem/ul/li[1]/div').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[3]/a').click()
            except:
                print("retry")
                driver.refresh()
                continue
            while(1):
                try:
                    time.sleep(5)
                    driver.find_element_by_css_selector('div.ui-grid-header > div > div > div > div > div > div.ui-grid-header-cell.ui-grid-clearfix.ui-grid-coluiGrid-0005 > div > div > div').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                    time.sleep(10)
                    try:
                        driver.find_element_by_xpath('//*[@id="shop_product_grid"]/div/div[2]/div[1]/div[1]/button[3]').click()
                    except:
                        break
                except:
                    break
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(3) > a > span'):
                print(j.string)
                if int(j.string)>0:
                    print("남아있다")
                    driver.get('https://app.playauto.io/#!/home')
                    break
                else:
                    return True

    
    def GSD(self):
        i=1
        excel=win32com.client.Dispatch("Excel.Application")
        excel.Visible=True
        url=self.PEEdit.text()
        wb=excel.workbooks.Open(url)
        ws=wb.ActiveSheet

        id=self.PEIDEdit.text()
        pw=self.PEPWEdit.text()
        driver.get('https://app.playauto.io/login.html')
        time.sleep(2)
        driver.find_element_by_name("email").send_keys(id)
        driver.find_element_by_name("password").send_keys(pw)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/form/div/div[5]/div/button').click()
        time.sleep(5)

        while(1):
            driver.get('https://app.playauto.io/#!/online/product/list')
            time.sleep(5)
            driver.refresh()
            time.sleep(5)
            while(1):
                try:
                    code=ws.Cells(i,1).Value
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(code)
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(Keys.ENTER)
                    i+=1
                    if ws.Cells(i,1).Value==None:
                        break
                except:
                    driver.refresh()
                    i=1
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[2]/div[1]/div/div/button').click()
            try:
                driver.find_element_by_xpath('//*[@id="online_product_grid_searchbar"]/div/ul/li[2]/a').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[3]/treeitem/ul/li[5]/i[1]').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[3]/treeitem/ul/li[5]/treeitem/ul/li[1]/div').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[3]/a').click()
            except:
                print("retry")
                driver.refresh()
                continue
            while(1):
                try:
                    time.sleep(5)
                    driver.find_element_by_css_selector('div.ui-grid-header > div > div > div > div > div > div.ui-grid-header-cell.ui-grid-clearfix.ui-grid-coluiGrid-0005 > div > div > div').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                    time.sleep(10)
                    try:
                        driver.find_element_by_xpath('//*[@id="shop_product_grid"]/div/div[2]/div[1]/div[1]/button[3]').click()
                    except:
                        break
                except:
                    break
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(3) > a > span'):
                print(j.string)
                if int(j.string)>0:
                    print("남아있다")
                    driver.get('https://app.playauto.io/#!/home')
                    break
                else:
                    return True


    def ASD(self):
        i=1
        excel=win32com.client.Dispatch("Excel.Application")
        excel.Visible=True
        url=self.PEEdit.text()
        wb=excel.workbooks.Open(url)
        ws=wb.ActiveSheet

        id=self.PEIDEdit.text()
        pw=self.PEPWEdit.text()
        driver.get('https://app.playauto.io/login.html')
        time.sleep(2)
        driver.find_element_by_name("email").send_keys(id)
        driver.find_element_by_name("password").send_keys(pw)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/form/div/div[5]/div/button').click()
        time.sleep(5)

        while(1):
            driver.get('https://app.playauto.io/#!/online/product/list')
            time.sleep(5)
            driver.refresh()
            time.sleep(5)
            while(1):
                try:
                    code=ws.Cells(i,1).Value
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(code)
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[5]/div/div[2]/textarea').send_keys(Keys.ENTER)
                    i+=1
                    if ws.Cells(i,1).Value==None:
                        break
                except:
                    driver.refresh()
                    i=1
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[2]/div[1]/div/div/button').click()
            try:
                driver.find_element_by_xpath('//*[@id="online_product_grid_searchbar"]/div/ul/li[2]/a').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[2]/treeitem/ul/li[5]/i[1]').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[2]/treeitem/ul/li[5]/treeitem/ul/li[1]/div').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[3]/a').click()
            except:
                print("retry")
                driver.refresh()
                continue
            while(1):
                try:
                    time.sleep(5)
                    driver.find_element_by_css_selector('div.ui-grid-header > div > div > div > div > div > div.ui-grid-header-cell.ui-grid-clearfix.ui-grid-coluiGrid-0005 > div > div > div').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                    time.sleep(10)
                    try:
                        driver.find_element_by_xpath('//*[@id="shop_product_grid"]/div/div[2]/div[1]/div[1]/button[3]').click()
                    except:
                        break
                except:
                    break
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(3) > a > span'):
                print(j.string)
                if int(j.string)>0:
                    print("남아있다")
                    time.sleep(60)
                    driver.get('https://app.playauto.io/#!/home')
                    break
                else:
                    return True




    def NHM(self):
        id=self.MIDEdit.text()
        pw=self.MPWEdit.text()

        driver.get('http://seller.nhmarket.kr/mallinmall/')

        driver.find_element_by_id('id').send_keys(id)
        driver.find_element_by_id('pass').send_keys(pw)
        driver.find_element_by_xpath('//*[@id="login_wrap"]/div[4]/img').click()

        time.sleep(2)

        while(1):
            driver.get('http://seller.nhmarket.kr/mallinmall/goods/goods_list.asp')

            driver.find_element_by_xpath('//*[@id="listsize"]/option[5]').click()
            driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/div[1]/img[7]').click()
            driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/div[1]/img[6]').click()

            Alert(driver).accept()
            Alert(driver).accept()
        return True

    def PAN(self):
        id='dolcevitamaster7@gmail.com'
        pw='akdntmzlqhem1@'
        driver.get('https://app.playauto.io/login.html')
        time.sleep(2)
        driver.find_element_by_name("email").send_keys(id)
        driver.find_element_by_name("password").send_keys(pw)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/form/div/div[5]/div/button').click()
        time.sleep(5)
        while(1):
            try:
                driver.get('https://app.playauto.io/#!/online/product/list')
                time.sleep(5)
                driver.find_element_by_xpath('//*[@id="online_product_grid_searchbar"]/div/ul/li[2]/a').click()
                time.sleep(5)
                html=driver.page_source
                soup=BeautifulSoup(html,'html.parser')
                for k in soup.select('div > treecontrol > ul > li:nth-child(2) > div'):
                    self.PANText.append(k.text)
                for i in range(2,3):
                    for k in soup.select('div > treecontrol > ul > li:nth-child(2) > treeitem > ul > li:nth-child('+str(i)+') > div'):
                        self.PANText.insertPlainText(k.text)
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[2]/treeitem/ul/li['+str(i)+']/i[1]').click()
                    for j in range(1,4):
                        html=driver.page_source
                        soup=BeautifulSoup(html,'html.parser')
                        for k in soup.select('treecontrol > ul > li:nth-child(2) > treeitem > ul > li:nth-child('+str(i)+') > treeitem > ul > li:nth-child('+str(j)+') > div'):
                            self.PANText.append(k.text)
                html=driver.page_source
                soup=BeautifulSoup(html,'html.parser')
                for k in soup.select('div > treecontrol > ul > li:nth-child(3) > div'):
                    self.PANText.append(k.text)
                for i in range(2,6):
                    for k in soup.select('div > treecontrol > ul > li:nth-child(3) > treeitem > ul > li:nth-child('+str(i)+') > div'):
                        self.PANText.append(k.text)
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[3]/treeitem/ul/li['+str(i)+']/i[1]').click()
                    for j in range(1,4):
                        html=driver.page_source
                        soup=BeautifulSoup(html,'html.parser')
                        for k in soup.select('treecontrol > ul > li:nth-child(3) > treeitem > ul > li:nth-child('+str(i)+') > treeitem > ul > li:nth-child('+str(j)+') > div'):
                            self.PANText.append(k.text)
                html=driver.page_source
                soup=BeautifulSoup(html,'html.parser')
                for k in soup.select('div > treecontrol > ul > li:nth-child(4) > div'):
                    self.PANText.append(k.text)
                for i in range(2,6):
                    for k in soup.select('div > treecontrol > ul > li:nth-child(4) > treeitem > ul > li:nth-child('+str(i)+') > div'):
                        self.PANText.append(k.text)
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[4]/treeitem/ul/li['+str(i)+']/i[1]').click()
                    for j in range(1,4):
                        html=driver.page_source
                        soup=BeautifulSoup(html,'html.parser')
                        for k in soup.select('treecontrol > ul > li:nth-child(4) > treeitem > ul > li:nth-child('+str(i)+') > treeitem > ul > li:nth-child('+str(j)+') > div'):
                            self.PANText.append(k.text)
                html=driver.page_source
                soup=BeautifulSoup(html,'html.parser')
                for k in soup.select('div > treecontrol > ul > li:nth-child(5) > div'):
                    self.PANText.append(k.text)
                for i in range(2,5):
                    for k in soup.select('div > treecontrol > ul > li:nth-child(5) > treeitem > ul > li:nth-child('+str(i)+') > div'):
                        self.PANText.append(k.text)
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[5]/treeitem/ul/li['+str(i)+']/i[1]').click()
                    for j in range(1,4):
                        html=driver.page_source
                        soup=BeautifulSoup(html,'html.parser')
                        for k in soup.select('treecontrol > ul > li:nth-child(5) > treeitem > ul > li:nth-child('+str(i)+') > treeitem > ul > li:nth-child('+str(j)+') > div'):
                            self.PANText.append(k.text)
                html=driver.page_source
                soup=BeautifulSoup(html,'html.parser')
                for k in soup.select('div > treecontrol > ul > li:nth-child(6) > div'):
                    self.PANText.append(k.text)
                for i in range(2,7):
                    for k in soup.select('div > treecontrol > ul > li:nth-child(6) > treeitem > ul > li:nth-child('+str(i)+') > div'):
                        self.PANText.append(k.text)
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[6]/treeitem/ul/li['+str(i)+']/i[1]').click()
                    for j in range(1,4):
                        html=driver.page_source
                        soup=BeautifulSoup(html,'html.parser')
                        for k in soup.select('treecontrol > ul > li:nth-child(6) > treeitem > ul > li:nth-child('+str(i)+') > treeitem > ul > li:nth-child('+str(j)+') > div'):
                            self.PANText.append(k.text)
                html=driver.page_source
                soup=BeautifulSoup(html,'html.parser')
                for k in soup.select('div > treecontrol > ul > li:nth-child(7) > div'):
                    self.PANText.append(k.text)
                for i in range(2,6):
                    for k in soup.select('div > treecontrol > ul > li:nth-child(7) > treeitem > ul > li:nth-child('+str(i)+') > div'):
                        self.PANText.append(k.text)
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[7]/treeitem/ul/li['+str(i)+']/i[1]').click()
                    for j in range(1,4):
                        html=driver.page_source
                        soup=BeautifulSoup(html,'html.parser')
                        for k in soup.select('treecontrol > ul > li:nth-child(7) > treeitem > ul > li:nth-child('+str(i)+') > treeitem > ul > li:nth-child('+str(j)+') > div'):
                            self.PANText.append(k.text)
                html=driver.page_source
                soup=BeautifulSoup(html,'html.parser')
                for k in soup.select('div > treecontrol > ul > li:nth-child(8) > div'):
                    self.PANText.append(k.text)
                for i in range(2,3):
                    for k in soup.select('div > treecontrol > ul > li:nth-child(8) > treeitem > ul > li:nth-child('+str(i)+') > div'):
                        self.PANText.append(k.text)
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[8]/treeitem/ul/li['+str(i)+']/i[1]').click()
                    for j in range(1,4):
                        html=driver.page_source
                        soup=BeautifulSoup(html,'html.parser')
                        for k in soup.select('treecontrol > ul > li:nth-child(8) > treeitem > ul > li:nth-child('+str(i)+') > treeitem > ul > li:nth-child('+str(j)+') > div'):
                            self.PANText.append(k.text)
                html=driver.page_source
                soup=BeautifulSoup(html,'html.parser')
                for k in soup.select('div > treecontrol > ul > li:nth-child(9) > div'):
                    self.PANText.append(k.text)
                for i in range(2,5):
                    for k in soup.select('div > treecontrol > ul > li:nth-child(9) > treeitem > ul > li:nth-child('+str(i)+') > div'):
                        self.PANText.append(k.text)
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[9]/treeitem/ul/li['+str(i)+']/i[1]').click()
                    for j in range(1,4):
                        html=driver.page_source
                        soup=BeautifulSoup(html,'html.parser')
                        for k in soup.select('treecontrol > ul > li:nth-child(9) > treeitem > ul > li:nth-child('+str(i)+') > treeitem > ul > li:nth-child('+str(j)+') > div'):
                            self.PANText.append(k.text)
                html=driver.page_source
                soup=BeautifulSoup(html,'html.parser')
                for k in soup.select('div > treecontrol > ul > li:nth-child(10) > div'):
                    self.PANText.append(k.text)
                for i in range(2,3):
                    for k in soup.select('div > treecontrol > ul > li:nth-child(10) > treeitem > ul > li:nth-child('+str(i)+') > div'):
                        self.PANText.append(k.text)
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[10]/treeitem/ul/li['+str(i)+']/i[1]').click()
                    for j in range(1,4):
                        html=driver.page_source
                        soup=BeautifulSoup(html,'html.parser')
                        for k in soup.select('treecontrol > ul > li:nth-child(10) > treeitem > ul > li:nth-child('+str(i)+') > treeitem > ul > li:nth-child('+str(j)+') > div'):
                            self.PANText.append(k.text)
                html=driver.page_source
                soup=BeautifulSoup(html,'html.parser')
                for k in soup.select('div > treecontrol > ul > li:nth-child(11) > div'):
                    self.PANText.append(k.text)
                for i in range(2,4):
                    for k in soup.select('div > treecontrol > ul > li:nth-child(11) > treeitem > ul > li:nth-child('+str(i)+') > div'):
                        self.PANText.append(k.text)
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[11]/treeitem/ul/li['+str(i)+']/i[1]').click()
                    for j in range(1,4):
                        html=driver.page_source
                        soup=BeautifulSoup(html,'html.parser')
                        for k in soup.select('treecontrol > ul > li:nth-child(11) > treeitem > ul > li:nth-child('+str(i)+') > treeitem > ul > li:nth-child('+str(j)+') > div'):
                            self.PANText.append(k.text)
                html=driver.page_source
                soup=BeautifulSoup(html,'html.parser')
                for k in soup.select('div > treecontrol > ul > li:nth-child(12) > div'):
                    self.PANText.append(k.text)
                for i in range(2,3):
                    for k in soup.select('div > treecontrol > ul > li:nth-child(12) > treeitem > ul > li:nth-child('+str(i)+') > div'):
                        self.PANText.append(k.text)
                    driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[12]/treeitem/ul/li['+str(i)+']/i[1]').click()
                    for j in range(1,4):
                        html=driver.page_source
                        soup=BeautifulSoup(html,'html.parser')
                        for k in soup.select('treecontrol > ul > li:nth-child(12) > treeitem > ul > li:nth-child('+str(i)+') > treeitem > ul > li:nth-child('+str(j)+') > div'):
                            self.PANText.append(k.text)
                break
            except:
                driver.refresh()
  
    def AE2(self):
        id=self.MIDEdit.text()
        pw=self.MPWEdit.text()
        driver.get('http://www.esmplus.com/Home/Home#TDM396')
        driver.find_element_by_id("Id").send_keys(id)
        driver.find_element_by_id("Password").send_keys(pw)
        driver.find_element_by_xpath('//*[@id="btnLogOn"]/img').click()
        time.sleep(2)
        driver.get("http://www.esmplus.com/Sell/SingleGoodsMng?menuCode=TDM396")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="divAcumlSum"]/table/tbody/tr[1]/td[5]/a').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="selPageSize"]/option[7]').click()
        time.sleep(2)
        while(1):
            driver.find_element_by_xpath('//*[@id="gridcolumn-1014-textEl"]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="goodsContents"]/div[1]/div[1]/div[1]/span[9]/a').click()
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            driver.maximize_window()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="aSave"]').click()
            driver.switch_to.alert.accept()
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(300)
            driver.find_element_by_xpath('//*[@id="popFooter"]/a').click()
            time.sleep(5)
            driver.switch_to.window(driver.window_handles[0])

    def AE1(self):
        id=self.MIDEdit.text()
        pw=self.MPWEdit.text()
        driver.get('http://www.esmplus.com/Home/Home#TDM396')
        driver.find_element_by_id("Id").send_keys(id)
        driver.find_element_by_id("Password").send_keys(pw)
        driver.find_element_by_xpath('//*[@id="btnLogOn"]/img').click()
        time.sleep(2)
        driver.get("http://www.esmplus.com/Sell/SingleGoodsMng?menuCode=TDM396")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="divAcumlSum"]/table/tbody/tr[1]/td[3]/a').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="selPageSize"]/option[7]').click()
        time.sleep(2)
        while(1):
            driver.find_element_by_xpath('//*[@id="gridcolumn-1014-textEl"]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="goodsContents"]/div[1]/div[1]/div[1]/span[2]/a').click()
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            driver.find_element_by_xpath('//*[@id="siteTypeIAC"]/input').click()
            driver.maximize_window()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="SellStateChangeStop"]').click()
            time.sleep(300)
            driver.switch_to.window(driver.window_handles[1])
            driver.find_element_by_xpath('//*[@id="popFooter"]/a/img').click()
            time.sleep(5)
            driver.switch_to.window(driver.window_handles[0])
    
    def GE1(self):
        id=self.MIDEdit.text()
        pw=self.MPWEdit.text()
        driver.get('http://www.esmplus.com/Home/Home#TDM396')
        driver.find_element_by_id("Id").send_keys(id)
        driver.find_element_by_id("Password").send_keys(pw)
        driver.find_element_by_xpath('//*[@id="btnLogOn"]/img').click()
        time.sleep(2)
        driver.get("http://www.esmplus.com/Sell/SingleGoodsMng?menuCode=TDM396")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="divAcumlSum"]/table/tbody/tr[2]/td[3]/a').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="selPageSize"]/option[7]').click()
        time.sleep(2)
        while(1):
            driver.find_element_by_xpath('//*[@id="gridcolumn-1014-textEl"]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="goodsContents"]/div[1]/div[1]/div[1]/span[2]/a').click()
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            driver.find_element_by_xpath('//*[@id="siteTypeGMKT"]/input').click()
            time.sleep(2)
            driver.maximize_window()
            driver.find_element_by_xpath('//*[@id="SellStateChangeStop"]').click()
            time.sleep(300)
            driver.switch_to.window(driver.window_handles[1])
            driver.find_element_by_xpath('//*[@id="popFooter"]/a/img').click()
            time.sleep(5)
            driver.switch_to.window(driver.window_handles[0])
    
    def GE2(self):
        id=self.MIDEdit.text()
        pw=self.MPWEdit.text()
        driver.get('http://www.esmplus.com/Home/Home#TDM396')
        driver.find_element_by_id("Id").send_keys(id)
        driver.find_element_by_id("Password").send_keys(pw)
        driver.find_element_by_xpath('//*[@id="btnLogOn"]/img').click()
        time.sleep(2)
        driver.get("http://www.esmplus.com/Sell/SingleGoodsMng?menuCode=TDM396")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="divAcumlSum"]/table/tbody/tr[2]/td[5]/a').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="selPageSize"]/option[7]').click()
        time.sleep(2)
        while(1):
            driver.find_element_by_xpath('//*[@id="gridcolumn-1014-textEl"]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="goodsContents"]/div[1]/div[1]/div[1]/span[9]/a').click()
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            driver.maximize_window()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="aSave"]').click()
            driver.switch_to.alert.accept()
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(300)
            driver.find_element_by_xpath('//*[@id="popFooter"]/a').click()
            time.sleep(5)
            driver.switch_to.window(driver.window_handles[0])

    def DBS(self):
        excel=win32com.client.Dispatch("Excel.Application")
        excel.Visible=True
        url=self.DExcelEdit.text()
        wb=excel.workbooks.Open(url)
        ws=wb.ActiveSheet

        i=2
        id="banyhousemaster"
        pw="qkqudtls123"
        driver.get("https://www.dometopia.com/member/login")
        driver.find_element_by_name("userid").send_keys(id)
        driver.find_element_by_name("password").send_keys(pw)
        driver.find_element_by_xpath('//*[@id="doto_login"]/div[3]/div[1]/form/div/input[3]').click()
        time.sleep(5)

        driver.get("http://www.dometopia.com/mypage/order_catalog")

        while(1):
            product=ws.Cells(i,2).Value
            driver.find_element_by_name("keyword").send_keys(product)
            driver.find_element_by_xpath('//*[@id="mypage-order_catalog"]/div[2]/form/div[2]/button').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="mypage-order_catalog"]/div[4]/table/tbody/tr/td[6]/span/span').click()
            time.sleep(5)
            try:
                driver.find_element_by_xpath('//*[@id="orderexportcontent"]/div/table/tbody/tr/td[4]/div[2]/button[2]').click()
                try:
                    driver.find_element_by_xpath('//*[@id="export_buy_confirm_msg"]/div[2]/label[1]/input').click()
                    time.sleep(5)
                    driver.find_element_by_xpath('//*[@id="export_buy_confirm_btn"]').click()
                    time.sleep(10)
                    driver.find_element_by_xpath('/html/body/div[10]/div[1]/a').click()
                    time.sleep(5)
                except:
                    driver.find_element_by_xpath('/html/body/div[8]/div[1]/a').click()
            except:
                driver.find_element_by_xpath('/html/body/div[8]/div[1]/a').click()
            driver.find_element_by_name("keyword").clear()
            i+=1
            if ws.Cells(i,2).Value==None:
                return True


    def DDS(self):
        excel=win32com.client.Dispatch("Excel.Application")
        excel.Visible=True
        url=self.DExcelEdit.text()
        wb=excel.workbooks.Open(url)
        ws=wb.ActiveSheet

        i=2
        id="dorothy385"
        pw="zlqhem12"
        driver.get("https://www.dometopia.com/member/login")
        driver.find_element_by_name("userid").send_keys(id)
        driver.find_element_by_name("password").send_keys(pw)
        driver.find_element_by_xpath('//*[@id="doto_login"]/div[3]/div[1]/form/div/input[3]').click()
        time.sleep(5)

        driver.get("http://www.dometopia.com/mypage/order_catalog")

        while(1):
            product=ws.Cells(i,2).Value
            driver.find_element_by_name("keyword").send_keys(product)
            driver.find_element_by_xpath('//*[@id="mypage-order_catalog"]/div[2]/form/div[2]/button').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="mypage-order_catalog"]/div[4]/table/tbody/tr/td[6]/span/span').click()
            time.sleep(5)
            try:
                driver.find_element_by_xpath('//*[@id="orderexportcontent"]/div/table/tbody/tr/td[4]/div[2]/button[2]').click()
                try:
                    driver.find_element_by_xpath('//*[@id="export_buy_confirm_msg"]/div[2]/label[1]/input').click()
                    time.sleep(5)
                    driver.find_element_by_xpath('//*[@id="export_buy_confirm_btn"]').click()
                    time.sleep(10)
                    driver.find_element_by_xpath('/html/body/div[10]/div[1]/a').click()
                    time.sleep(5)
                except:
                    driver.find_element_by_xpath('/html/body/div[8]/div[1]/a').click()
            except:
                driver.find_element_by_xpath('/html/body/div[8]/div[1]/a').click()
            driver.find_element_by_name("keyword").clear()
            i+=1
            if ws.Cells(i,2).Value==None:
                return True

    def DSS(self):
        excel=win32com.client.Dispatch("Excel.Application")
        excel.Visible=True
        url=self.DExcelEdit.text()
        wb=excel.workbooks.Open(url)
        ws=wb.ActiveSheet

        i=2
        id="yoome123"
        pw="dowk123"
        driver.get("https://www.dometopia.com/member/login")
        driver.find_element_by_name("userid").send_keys(id)
        driver.find_element_by_name("password").send_keys(pw)
        driver.find_element_by_xpath('//*[@id="doto_login"]/div[3]/div[1]/form/div/input[3]').click()
        time.sleep(5)

        driver.get("http://www.dometopia.com/mypage/order_catalog")

        while(1):
            product=ws.Cells(i,2).Value
            driver.find_element_by_name("keyword").send_keys(product)
            driver.find_element_by_xpath('//*[@id="mypage-order_catalog"]/div[2]/form/div[2]/button').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="mypage-order_catalog"]/div[4]/table/tbody/tr/td[6]/span/span').click()
            time.sleep(5)
            try:
                driver.find_element_by_xpath('//*[@id="orderexportcontent"]/div/table/tbody/tr/td[4]/div[2]/button[2]').click()
                try:
                    driver.find_element_by_xpath('//*[@id="export_buy_confirm_msg"]/div[2]/label[1]/input').click()
                    time.sleep(5)
                    driver.find_element_by_xpath('//*[@id="export_buy_confirm_btn"]').click()
                    time.sleep(10)
                    driver.find_element_by_xpath('/html/body/div[10]/div[1]/a').click()
                    time.sleep(5)
                except:
                    driver.find_element_by_xpath('/html/body/div[8]/div[1]/a').click()
            except:
                driver.find_element_by_xpath('/html/body/div[8]/div[1]/a').click()
            driver.find_element_by_name("keyword").clear()
            i+=1
            if ws.Cells(i,2).Value==None:
                return True

    def DDP(self):
        excel=win32com.client.Dispatch("Excel.Application")
        excel.Visible=True
        url=self.DExcelEdit.text()
        wb=excel.workbooks.Open(url)
        ws=wb.ActiveSheet

        id='dorothy385'
        pw='zlqhem12'

        driver.get('http://dometopia.com/member/login')
        driver.find_element_by_name("userid").send_keys(id)
        driver.find_element_by_name("password").send_keys(pw)
        driver.find_element_by_xpath('//*[@id="doto_login"]/div[3]/div[1]/form/div/input[3]').click()
        time.sleep(5)

        for i in range(2,int(ws.Cells(1,1).Value)+2):
            number=ws.Cells(i,1).Value
            driver.get('http://dometopia.com/goods/search?search_text='+str(int(number)))
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for j in soup.select('table > tbody > tr > td > dl > dd > span > b'):
                ws.Cells(i,2).Value=j.string
        
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())