import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTreeWidgetItem, QDesktopWidget, qApp
import PyQt5.QtCore as Core
from mainwindow import Ui_MainWindow
from accounts import Ui_MainWindow as AccountWindow


class TMail_Accounts(QMainWindow):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = AccountWindow()
        self.ui.setupUi(self)


class TMail(QMainWindow):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #SET WINDOW TO SCREEN CENTER
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.accounts = TMail_Accounts()
        self.ui.actionNew_account.triggered.connect(self.onAccounts)
        self.ui.actionExit.triggered.connect(qApp.exit)
        self.addItems(self.ui.treeWidget.invisibleRootItem())

    def addItems(self, parent):
        column = 0
        inbox_branch = self.addParent(parent, column, 'Inbox', 'data Inbox')
        outbox_branch = self.addParent(parent, column, 'Outbox', 'data Outbox')

        self.addChild(inbox_branch, column, 'Main', 'data Type 1')
        self.addChild(inbox_branch, column, 'Spam', 'data Type 2')

        self.addChild(outbox_branch, column, 'Sent', 'data Type 3')
        self.addChild(outbox_branch, column, 'Drafts', 'data Type 4')


    def addParent(self, parent, column, title, data):
        item = QTreeWidgetItem(parent, [title])
        item.setData(column, Core.Qt.UserRole, data)
        item.setChildIndicatorPolicy(QTreeWidgetItem.ShowIndicator)
        item.setExpanded(True)
        return item

    def addChild(self, parent, column, title, data):
        item = QTreeWidgetItem(parent, [title])
        item.setData(column, Core.Qt.UserRole, data)
        return item

    def onAccounts(self):
        qtRectangle = self.frameGeometry()
        self.accounts.move(qtRectangle.topLeft())
        self.accounts.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyApp = TMail()
    MyApp.show();
    sys.exit(app.exec_())