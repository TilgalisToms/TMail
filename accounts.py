from PyQt5.QtWidgets import QTableWidgetItem,QMainWindow
from PyQt5.Qt import Qt
from window_accounts import Ui_AccountsWindow
import database as DB
from edit_account import TMail_EditAccount as EditAccountWindow

class TMail_Accounts(QMainWindow):

    accountArray = {}

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.ui = Ui_AccountsWindow()
        self.ui.setupUi(self)
        self.ui.actionClose.triggered.connect(self.close)
        self.editAccount = EditAccountWindow(self)
        table = self.ui.tableWidget
        table.setColumnWidth(0,530)
        addAccount = self.ui.pushButton
        addAccount.clicked.connect(self.createRow)
        table.cellClicked.connect(self.selectColumn)
        self.db = DB.Database()
        self.loadAccounts()

    def selectColumn(self):
        qtRectangle = self.frameGeometry()
        self.editAccount.move(qtRectangle.topLeft())
        self.editAccount.activeAccount = self.ui.tableWidget.currentItem().data(Qt.UserRole)
        exists = self.editAccount.getAccount()
        if exists != False:
            self.editAccount.show()

    def loadAccounts(self):
        mailboxes = self.getMailboxes()
        for index,mailbox in mailboxes.items():
            lastIndex = self.ui.tableWidget.rowCount()
            table = self.ui.tableWidget
            table.insertRow(lastIndex)
            item = QTableWidgetItem(mailbox['address'])
            item.setData(Qt.UserRole,mailbox['id'])
            table.setItem(lastIndex, 0, item)

    def createRow(self):
        lastIndex = self.ui.tableWidget.rowCount()
        table = self.ui.tableWidget
        table.insertRow(lastIndex)
        item = QTableWidgetItem("E-mail address")
        item.setData(Qt.UserRole,None)#This means we create new account
        table.setItem(lastIndex,0,item)

    def getMailboxes(self):
        if len(self.accountArray) == 0:
            self.accountArray = self.db.getMailboxes()
        return self.accountArray

    def refresh(self):
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setRowCount(0)
        self.loadAccounts()
        self.parent.refresh()