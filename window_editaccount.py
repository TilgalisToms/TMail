# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/doublet/QT5/Email/editaccount.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditAccount(object):
    def setupUi(self, EditAccount):
        EditAccount.setObjectName("EditAccount")
        EditAccount.resize(280, 240)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EditAccount.sizePolicy().hasHeightForWidth())
        EditAccount.setSizePolicy(sizePolicy)
        EditAccount.setMinimumSize(QtCore.QSize(280, 240))
        EditAccount.setMaximumSize(QtCore.QSize(280, 240))
        self.centralwidget = QtWidgets.QWidget(EditAccount)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 5, 221, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 62, 221, 16))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 119, 221, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 180, 90, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_del = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_del.setGeometry(QtCore.QRect(180, 180, 90, 25))
        self.pushButton_del.setObjectName("pushButton_del")
        self.lineEdit_email = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_email.setGeometry(QtCore.QRect(10, 26, 260, 31))
        self.lineEdit_email.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_email.setClearButtonEnabled(False)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.lineEdit_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pass.setGeometry(QtCore.QRect(10, 83, 260, 31))
        self.lineEdit_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_pass.setClearButtonEnabled(False)
        self.lineEdit_pass.setObjectName("lineEdit_pass")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(10, 140, 260, 31))
        self.lineEdit_name.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_name.setClearButtonEnabled(False)
        self.lineEdit_name.setObjectName("lineEdit_name")
        EditAccount.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EditAccount)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 280, 19))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        EditAccount.setMenuBar(self.menubar)
        self.actionClose = QtWidgets.QAction(EditAccount)
        self.actionClose.setObjectName("actionClose")
        self.menuMenu.addAction(self.actionClose)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(EditAccount)
        QtCore.QMetaObject.connectSlotsByName(EditAccount)

    def retranslateUi(self, EditAccount):
        _translate = QtCore.QCoreApplication.translate
        EditAccount.setWindowTitle(_translate("EditAccount", "MainWindow"))
        self.label.setText(_translate("EditAccount", "E-Mail address"))
        self.label_2.setText(_translate("EditAccount", "E-Mail password"))
        self.label_5.setText(_translate("EditAccount", "Account name"))
        self.pushButton.setText(_translate("EditAccount", "Save"))
        self.pushButton_del.setText(_translate("EditAccount", "Delete"))
        self.menuMenu.setTitle(_translate("EditAccount", "Menu"))
        self.actionClose.setText(_translate("EditAccount", "Close"))

