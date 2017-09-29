import sys
import accounts as AccountWindow
import database as DB

from PyQt5.QtWidgets import QApplication,QMainWindow,QTreeWidgetItem,QDesktopWidget,qApp
from window_main import Ui_MainWindow

class TMail(QMainWindow):

    def __init__(self, parent=None):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = DB.Database()
        #INITIAL WIDTH
        self.initialMainGeometry = self.frameGeometry()

        #SET TO WINDOW CENTER
        centerPoint = QDesktopWidget().availableGeometry().center()
        self.initialMainGeometry.moveCenter(centerPoint)
        self.move(self.initialMainGeometry.topLeft())

        self.accounts = AccountWindow.TMail_Accounts()
        self.ui.actionNew_account.triggered.connect(self.onAccounts)
        self.ui.actionExit.triggered.connect(qApp.exit)
        self.addItems(self.ui.treeWidget.invisibleRootItem())

    def addItems(self, parent):
        column = 0
        mailboxes = self.db.getMailboxes()
        for mailbox in mailboxes:
            rootParent = self.addParent(parent, column, mailbox[0])
            inbox_branch = self.addChild(rootParent, column, 'Inbox')
            outbox_branch = self.addChild(rootParent, column, 'Outbox')

            self.addChild(inbox_branch, column, 'Main')
            self.addChild(inbox_branch, column, 'Spam')

            self.addChild(outbox_branch, column, 'Sent')
            self.addChild(outbox_branch, column, 'Drafts')

    def addParent(self, parent, column, title):
        item = QTreeWidgetItem(parent, [title])
        item.setChildIndicatorPolicy(QTreeWidgetItem.ShowIndicator)
        item.setExpanded(True)
        return item

    def addChild(self, parent, column, title):
        item = QTreeWidgetItem(parent, [title])
        return item

    def onAccounts(self):
        qtRectangle = self.frameGeometry()
        self.accounts.move(qtRectangle.topLeft())
        self.accounts.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyApp = TMail()
    MyApp.show()
    sys.exit(app.exec_())