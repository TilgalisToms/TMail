from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(651, 361)
        MainWindow.setMinimumSize(QtCore.QSize(650, 360))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        mainLayout = QtWidgets.QGridLayout()
        mainLayout.setColumnStretch(0,1)
        mainLayout.setColumnStretch(1,3)
        mainLayout.setColumnMinimumWidth(1,460)
        mainLayout.setContentsMargins(10, 10, 10, 10)

        leftLayout = QtWidgets.QHBoxLayout()
        rightLayout = QtWidgets.QVBoxLayout()
        rightTopLayout = QtWidgets.QHBoxLayout()
        rightBottomLayout = QtWidgets.QHBoxLayout()

        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 10, 89, 20))
        self.pushButton.setObjectName("pushButton")
        rightTopLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 10, 89, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        rightTopLayout.addWidget(self.pushButton_2)

        self.treeWidget = QtWidgets.QTreeWidget()
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "E-Mail")
        leftLayout.addWidget(self.treeWidget)

        self.listWidget = QtWidgets.QListWidget()
        self.listWidget.setObjectName("listWidget")
        rightBottomLayout.addWidget(self.listWidget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 651, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuTMail = QtWidgets.QMenu(self.menuBar)
        self.menuTMail.setObjectName("menuTMail")
        MainWindow.setMenuBar(self.menuBar)
        self.actionNew_account = QtWidgets.QAction(MainWindow)
        self.actionNew_account.setObjectName("actionNew_account")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuTMail.addAction(self.actionNew_account)
        self.menuTMail.addSeparator()
        self.menuTMail.addAction(self.actionExit)
        self.menuBar.addAction(self.menuTMail.menuAction())

        mainLayout.addLayout(leftLayout,0,0)
        rightLayout.addLayout(rightTopLayout)
        rightLayout.addLayout(rightBottomLayout)
        mainLayout.addLayout(rightLayout,0,1)

        self.centralWidget.setLayout(mainLayout)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Compose"))
        self.pushButton_2.setText(_translate("MainWindow", "Refresh"))
        self.menuTMail.setTitle(_translate("MainWindow", "Menu"))
        self.actionNew_account.setText(_translate("MainWindow", "Accounts"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

