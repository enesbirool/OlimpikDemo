# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Birol/Desktop/ESSK/assets/GUI/psiko_panel.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(833, 501)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/assets/olimpik.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setMouseTracking(False)
        self.tableWidget.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(12)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.sporcutc_name_surname = QtWidgets.QLabel(Form)
        self.sporcutc_name_surname.setText("")
        self.sporcutc_name_surname.setObjectName("sporcutc_name_surname")
        self.horizontalLayout.addWidget(self.sporcutc_name_surname)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.psiko_add_button = QtWidgets.QPushButton(Form)
        self.psiko_add_button.setObjectName("psiko_add_button")
        self.horizontalLayout.addWidget(self.psiko_add_button)
        self.excel_aktar_button = QtWidgets.QPushButton(Form)
        self.excel_aktar_button.setObjectName("excel_aktar_button")
        self.horizontalLayout.addWidget(self.excel_aktar_button)
        self.sayfa_yenile_button = QtWidgets.QPushButton(Form)
        self.sayfa_yenile_button.setObjectName("sayfa_yenile_button")
        self.horizontalLayout.addWidget(self.sayfa_yenile_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Psikomotor Panel"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "TC"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Adı"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Soyadı"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Boy"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Kilo"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Tarih"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Denge"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Uzun Atlama"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Dikey Sıçrama"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Form", "Esneklik"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Form", "30 Metre"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("Form", "100 Metre"))
        self.label.setText(_translate("Form", "SEÇİLİ SPORCU TC/ADI/SOYADI :"))
        self.psiko_add_button.setText(_translate("Form", "Psikomotor Ekle"))
        self.excel_aktar_button.setText(_translate("Form", "Excel\'e Aktar"))
        self.sayfa_yenile_button.setText(_translate("Form", "Sayfayı Yenile"))

import assets.py_rc.icons_rc as icons_rc
