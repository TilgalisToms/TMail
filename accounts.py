from PyQt5.QtWidgets import QTableWidgetItem,QMainWindow
from window_accounts import Ui_AccountsWindow
import database as DB
from edit_account import TMail_EditAccount as EditAccountWindow

class TMail_Accounts(QMainWindow):

    accountArray = []

    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_AccountsWindow()
        self.ui.setupUi(self)
        self.ui.actionClose.triggered.connect(self.close)
        self.editAccount = EditAccountWindow()
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
        self.editAccount.show()

    def loadAccounts(self):
        mailboxes = self.getMailboxes()
        for mailbox in mailboxes:
            lastIndex = self.ui.tableWidget.rowCount()
            table = self.ui.tableWidget
            table.insertRow(lastIndex)
            table.setItem(lastIndex, 0, QTableWidgetItem(mailbox[0]))

    def createRow(self):
        lastIndex = self.ui.tableWidget.rowCount()
        table = self.ui.tableWidget
        table.insertRow(lastIndex)
        table.setItem(lastIndex,0,QTableWidgetItem("E-mail address"))

    def getMailboxes(self):
        if self.accountArray.__len__() == 0:
            self.accountArray = self.db.getMailboxes()
        return self.accountArray