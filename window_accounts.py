from PyQt5 import QtCore, QtWidgets

class Ui_AccountsWindow(object):
    def setupUi(self, AccountsWindow):
        AccountsWindow.setObjectName("AccountsWindow")
        AccountsWindow.resize(540, 312)
        AccountsWindow.setMinimumSize(QtCore.QSize(540, 312))
        AccountsWindow.setMaximumSize(QtCore.QSize(540, 312))
        self.centralwidget = QtWidgets.QWidget(AccountsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(5, 40, 530, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(530, 221))
        self.tableWidget.setMaximumSize(QtCore.QSize(541, 221))
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(443, 10, 91, 21))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(350, 10, 91, 21))
        self.pushButton_save.setObjectName("pushButton_save")
        AccountsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AccountsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 22))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        AccountsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AccountsWindow)
        self.statusbar.setObjectName("statusbar")
        AccountsWindow.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(AccountsWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuMenu.addAction(self.actionClose)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(AccountsWindow)
        QtCore.QMetaObject.connectSlotsByName(AccountsWindow)

    def retranslateUi(self, AccountsWindow):
        _translate = QtCore.QCoreApplication.translate
        AccountsWindow.setWindowTitle(_translate("AccountsWindow", "MainWindow"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("AccountsWindow", "E-Mail address"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("AccountsWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("AccountsWindow", "Delete account"))
        self.pushButton.setText(_translate("AccountsWindow", "Add new"))
        self.pushButton_save.setText(_translate("AccountsWindow", "Save"))
        self.menuMenu.setTitle(_translate("AccountsWindow", "Menu"))
        self.actionClose.setText(_translate("AccountsWindow", "Close"))

