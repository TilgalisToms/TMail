import sys
import accounts as AccountWindow
import imaplib as Imap
import pickle

from PyQt5.QtWidgets import QApplication,QMainWindow,QTreeWidgetItem,QDesktopWidget,qApp
from window_main import Ui_MainWindow

class TMail(QMainWindow):

    folders = {}

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
            rootParent = self.addParent(parent, column, mailbox['address'])

            inbox_branch = self.addChild(rootParent, column, 'Inbox')
            outbox_branch = self.addChild(rootParent, column, 'Outbox')
            self.folders['inbox'] = self.addChild(inbox_branch, column, 'Main')
            self.folders['spam'] = self.addChild(inbox_branch, column, 'Spam')
            self.folders['sent'] = self.addChild(outbox_branch, column, 'Sent')
            self.folders['drafts'] = self.addChild(outbox_branch, column, 'Drafts')
            # @todo create and import cache -> sync
            imap = mailbox['imap'].split(':')
            connection = Imap.IMAP4_SSL(imap[0],imap[1])
            connection.login(mailbox['address'],mailbox['password'])
            for folder in connection.list()[1]:
                folder_data = folder.decode().split(' "/" ')
                #HARD-CODED Google MAIL STUFF
                if folder_data[1] == 'INBOX':
                    self.fetchInbox()
                if folder_data[1] == '[Gmail]/Spam':
                    self.fetchSpam()
                if folder_data[1] == '[Gmail]/Sent Mail':
                    self.fetchSent()
                if folder_data[1] == '[Gmail]/Drafts':
                    self.fetchDrafts()
                # connection.select(folder_data[1])
                # result, data = connection.search(None, "ALL")
                # ids = data[0]  # data is a list.
                # id_list = ids.split()  # ids is a space separated string
                # latest_email_id = id_list[-1]  # get the latest
                #
                # result, data = connection.fetch(latest_email_id, "(RFC822)")  # fetch the email body (RFC822) for the given ID


    def fetchInbox(self):
        return []

    def fetchSpam(self):
        return []

    def fetchSent(self):
        return []

    def fetchDrafts(self):
        return []

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
    app = QApplication(sys.argv)
    MyApp = TMail()
    MyApp.show()
    sys.exit(app.exec_())