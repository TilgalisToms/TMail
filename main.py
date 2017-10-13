import sys
import accounts as AccountWindow
from gmail import GMail

from PyQt5.QtWidgets import QApplication,QMainWindow,QTreeWidgetItem,QDesktopWidget,qApp
from window_main import Ui_MainWindow


class TMail(QMainWindow):

    folders = {}
    mailbox = {}

    def __init__(self, parent=None):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #INITIAL WIDTH
        self.initialMainGeometry = self.frameGeometry()

        #SET TO WINDOW CENTER
        centerPoint = QDesktopWidget().availableGeometry().center()
        self.initialMainGeometry.moveCenter(centerPoint)
        self.move(self.initialMainGeometry.topLeft())

        self.accounts = AccountWindow.TMail_Accounts(self)
        self.ui.actionNew_account.triggered.connect(self.onAccounts)
        self.ui.actionExit.triggered.connect(qApp.exit)
        self.addItems(self.ui.treeWidget.invisibleRootItem())

    def addItems(self, parent):
        column = 0
        mailboxes = self.accounts.getMailboxes()
        for index,mailbox in mailboxes.items():
            self.mailbox[mailbox['address']] = GMail(self)
            login = self.mailbox[mailbox['address']].login(mailbox['address'],mailbox['password'])
            if login == True:
                rootParent = self.addParent(parent, column, mailbox['address'])
                inbox_branch = self.addChild(rootParent, column, 'Inbox')
                outbox_branch = self.addChild(rootParent, column, 'Outbox')
                self.folders['inbox'] = self.addChild(inbox_branch, column, 'Main')
                self.folders['spam'] = self.addChild(inbox_branch, column, 'Spam')
                self.folders['sent'] = self.addChild(outbox_branch, column, 'Sent')
                self.folders['drafts'] = self.addChild(outbox_branch, column, 'Drafts')
                self.mailbox[mailbox['address']].fetchMail()
    def addParent(self, parent, column, title):
        item = QTreeWidgetItem(parent, [title])
        item.setChildIndicatorPolicy(QTreeWidgetItem.ShowIndicator)
        item.setExpanded(True)
        return item

    def addChild(self, parent, column, title):
        item = QTreeWidgetItem(parent, [title])
        item.setExpanded(True)
        return item

    def onAccounts(self):
        qtRectangle = self.frameGeometry()
        self.accounts.move(qtRectangle.topLeft())
        self.accounts.show()

    def refresh(self):
        self.ui.treeWidget.clear()
        self.addItems(self.ui.treeWidget.invisibleRootItem())


if __name__ == '__main__':
    #@todo Move sync and other logic after client UI has already rendered (cool loading icons for fetching and stuff)
    app = QApplication(sys.argv)
    MyApp = TMail()
    MyApp.show()
    sys.exit(app.exec_())