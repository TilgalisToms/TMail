from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox,QMainWindow,QInputDialog,QLineEdit
from PyQt5.QtGui import QBrush, QColor
import PyQt5.Qt as Qt
from window_accounts import Ui_AccountsWindow
import PyQt5.QtCore as Core
import database as DB

class TMail_Accounts(QMainWindow):

    accountArray = []
    maskedPlaceholder = '********'

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
        table.cellClicked.connect(self.selectColumn)
        self.ui.pushButton_save.clicked.connect(self.saveAccounts)
        self.db = DB.Database()
        self.loadAccounts()

    def selectColumn(self):
        currentColumn = self.ui.tableWidget.currentColumn()
        if currentColumn == 2:
            self.MessageBox()
        if currentColumn == 1:
            if self.ui.tableWidget.currentItem().text() == self.maskedPlaceholder:
                self.PasswordBox()
            else:
                self.ui.tableWidget.currentItem().setText(self.maskedPlaceholder)

    def loadAccounts(self):
        mailboxes = self.getMailboxes()
        for mailbox in mailboxes:
            lastIndex = self.ui.tableWidget.rowCount()
            table = self.ui.tableWidget
            table.insertRow(lastIndex)
            table.setItem(lastIndex, 0, QTableWidgetItem(mailbox[1]))
            passwordItem = QTableWidgetItem(self.maskedPlaceholder)
            passwordItem.setData(Core.Qt.UserRole,mailbox[2])
            table.setItem(lastIndex, 1, passwordItem)
            item = QTableWidgetItem("Delete")
            item.setForeground(QBrush(QColor(85, 0, 0, 255)))
            item.setFlags(Core.Qt.ItemIsEnabled)
            table.setItem(lastIndex, 2, item)

    def MessageBox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)

        msg.setText("Deleting E-Mail account")
        msg.setInformativeText("Are You sure You want to do this?")
        msg.setWindowTitle("TMail - Account")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.buttonClicked.connect(self.confirmed)
        msg.exec_()

    def PasswordBox(self):
        masterPassword = self.db.getConfigValue('master')
        if masterPassword == False:
            #There is no master password
            text_2, okPressed_2 = QInputDialog.getText(self, 'Set Master Password',
                                                       "Enter New Master password and DON'T forget it:",
                                                       QLineEdit.Normal, "")
            if okPressed_2 == True and text_2 != '':
                self.db.setConfigValue('master', text_2)
        else:
            text, okPressed = QInputDialog.getText(self,'Master Password','Enter Master password:',QLineEdit.Normal, "")
            if okPressed == True and text != '' and masterPassword != False and masterPassword == text:
                #we entered correctly
                self.ui.tableWidget.currentItem().setText(self.ui.tableWidget.currentItem().data(Core.Qt.UserRole))
            if masterPassword != False and masterPassword != text:
                #incorrect password
                self.ui.tableWidget.currentItem().setText('Incorrect password')


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

    def getMailboxes(self):
        if self.accountArray.__len__() == 0:
            self.accountArray = self.db.getMailboxes(True)
        return self.accountArray