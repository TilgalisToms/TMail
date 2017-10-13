from PyQt5.QtWidgets import QMainWindow
from window_editaccount import Ui_EditAccount
import database as DB
import re

class TMail_EditAccount(QMainWindow):

    activeAccount = 0

    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_EditAccount()
        self.ui.setupUi(self)
        self.ui.actionClose.triggered.connect(self.close)
        self.ui.pushButton.clicked.connect(self.saveAccount)
        self.parent = parent
        self.ui.pushButton_del.clicked.connect(self.deleteAccount)
        self.db = DB.Database()

    def getAccount(self):
        if self.activeAccount == '':
            return False
        if self.activeAccount != None:
            self.activeAccount = self.db.getMailbox(self.activeAccount)
            self.ui.lineEdit_email.setText(self.activeAccount['address'])
            if self.activeAccount['password'] != None:
                self.ui.lineEdit_pass.setText(self.activeAccount['password'])
            if self.activeAccount['title'] != None:
                self.ui.lineEdit_name.setText(self.activeAccount['title'])

    def saveAccount(self):
        errors = 0
        self.saveData = {}
        self.saveData['password'] = self.ui.lineEdit_pass.text()
        self.saveData['title']    = self.ui.lineEdit_name.text()
        if re.match(r"[^@]+@[^@]+\.[^@]+",self.ui.lineEdit_email.text()):
            self.saveData['email'] = self.ui.lineEdit_email.text()
        else:
            self.ui.label.setText(self.ui.label.text() + ' is INVALID!')
            self.ui.label.setStyleSheet('color: red')
            errors += 1

        if errors == 0:
            #@todo create account setting validity check against IMAP and SMTP here
            if self.activeAccount == None:
                self.db.createAccount(self.saveData)
            else:
                self.db.saveAccount(self.activeAccount['id'], self.saveData)
            self.refresh()
            self.close()

    def deleteAccount(self):
        self.db.removeMailbox(self.activeAccount['id'])
        del(self.parent.accountArray[self.activeAccount['id']])
        self.refresh()
        self.close()

    def refresh(self):
        self.parent.refresh()

    def validateUrl(self,text):
        return re.match(r"(([a-zA-Z0-9]+(-[a-zA-Z0-9]+)*\.)+[a-z]{2,10}:[0-9]{2,5})", text)