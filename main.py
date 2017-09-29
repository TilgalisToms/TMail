import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTreeWidgetItem, QDesktopWidget, \
    qApp, QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QBrush, QColor
import PyQt5.QtCore as Core
from mainwindow import Ui_MainWindow
from accounts import Ui_AccountsWindow

class TMail_Accounts(QMainWindow):

    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_AccountsWindow()
        self.ui.setupUi(self)
        self.ui.actionClose.triggered.connect(self.close)
        table = self.ui.tableWidget
        table.setColumnCount(3)
        table.setColumnWidth(0,225)
        table.setColumnWidth(1,225)
        table.setColumnWidth(2,70)
        addAccount = self.ui.pushButton
        addAccount.clicked.connect(self.createRow)
        table.cellClicked.connect(self.foo)
        self.ui.pushButton_save.clicked.connect(self.saveAccounts)

    def foo(self):
        currentColumn = self.ui.tableWidget.currentColumn()
        if currentColumn == 2:
            self.MessageBox()

    def MessageBox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)

        msg.setText("Deleting E-Mail account")
        msg.setInformativeText("Are You sure You want to do this?")
        msg.setWindowTitle("TMail - Account")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.buttonClicked.connect(self.confirmed)
        msg.exec_()

    def confirmed(self,i):
        if i.text() == 'OK':
            self.ui.tableWidget.removeRow(self.ui.tableWidget.currentRow())


    def createRow(self):
        lastIndex = self.ui.tableWidget.rowCount()
        table = self.ui.tableWidget
        table.insertRow(lastIndex)
        table.setItem(lastIndex,0,QTableWidgetItem("E-mail address"))
        table.setItem(lastIndex,1,QTableWidgetItem("E-mail password"))
        item = QTableWidgetItem("Delete")
        item.setForeground(QBrush(QColor(85,0,0,255)))
        item.setFlags(Core.Qt.ItemIsEnabled)
        table.setItem(lastIndex,2,item)

    def saveAccounts(self):
        table = self.ui.tableWidget


class TMail(QMainWindow):

    def __init__(self, parent=None):
        super().__init__()
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
        inbox_branch = self.addParent(parent, column, 'Inbox')
        outbox_branch = self.addParent(parent, column, 'Outbox')

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
    MyApp.show();
    sys.exit(app.exec_())