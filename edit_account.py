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
            # 0-ID,1-Address,2-Password,3-IMAP,4-SMTP,5-Title
            self.ui.lineEdit_email.setText(self.activeAccount['address'])
            if self.activeAccount['password'] != None:
                self.ui.lineEdit_pass.setText(self.activeAccount['password'])
            if self.activeAccount['imap'] != None:
                self.ui.lineEdit_imap.setText(self.activeAccount['imap'])
            if self.activeAccount['smtp'] != None:
                self.ui.lineEdit_smtp.setText(self.activeAccount['smtp'])
            if self.activeAccount['title'] != None:
                self.ui.lineEdit_name.setText(self.activeAccount['title'])

    def saveAccount(self):
        errors = 0
        self.saveData = {}
        self.saveData['password'] = self.ui.lineEdit_pass.text()
        self.saveData['title']    = self.ui.lineEdit_name.text()
        #@todo move validation and data fill in one method
        if re.match(r"[^@]+@[^@]+\.[^@]+",self.ui.lineEdit_email.text()):
            self.saveData['email'] = self.ui.lineEdit_email.text()
        else:
            self.ui.label.setText(self.ui.label.text() + ' is INVALID!')
            self.ui.label.setStyleSheet('color: red')
            errors += 1

        if self.validateUrl(self.ui.lineEdit_imap.text()):
            self.saveData['imap'] = self.ui.lineEdit_imap.text()
        else:
            self.ui.label_3.setText(self.ui.label_3.text() + ' is INVALID')
            self.ui.label_3.setStyleSheet('color: red')
            errors += 1

        if self.validateUrl(self.ui.lineEdit_smtp.text()):
            self.saveData['smtp'] = self.ui.lineEdit_smtp.text()
        else:
            self.ui.label_4.setText(self.ui.label_4.text() +  ' is INVALID')
            self.ui.label_4.setStyleSheet('color: red')
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