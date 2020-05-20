# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'barcode.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(453, 305)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 191, 21))
        self.label.setStyleSheet("font-family:helvetica;\n"
"font-size:15px;\n"
"font-weight:bold;")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 230, 131, 21))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(230, 70, 171, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 81, 20))
        self.label_2.setStyleSheet("font-size:12px;")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 180, 171, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 180, 141, 16))
        self.label_3.setStyleSheet("font-size:12px;")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 120, 171, 20))
        self.lineEdit_2.setToolTip("")
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 120, 171, 16))
        self.label_5.setToolTip("")
        self.label_5.setStyleSheet("font-size:12px;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(100, 140, 371, 20))
        self.label_6.setStyleSheet("color:Red;")
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 453, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Barcode Generator"))
        self.label.setText(_translate("MainWindow", "BARCODE GENERATOR"))
        self.pushButton.setText(_translate("MainWindow", "GENERATE"))
        self.comboBox.setItemText(0, _translate("MainWindow", "CODE128"))
        self.comboBox.setItemText(1, _translate("MainWindow", "ISBN13"))
        self.comboBox.setItemText(2, _translate("MainWindow", "CODE39"))
        self.comboBox.setItemText(3, _translate("MainWindow", "EAN14"))
        self.comboBox.setItemText(4, _translate("MainWindow", "EAN13"))
        self.label_2.setText(_translate("MainWindow", "Barcode Type"))
        self.label_3.setText(_translate("MainWindow", "Number of Barcode"))
        self.label_5.setText(_translate("MainWindow", "Barcode Start With (4 Digit)"))
        self.label_6.setText(_translate("MainWindow", "(If selected CODE128 or CODE39, type this)"))
