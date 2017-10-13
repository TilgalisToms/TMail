import imaplib
import email
from database import Database

class GMail:

    messages = {}

    def __init__(self,parent=None):
        self.connection = imaplib.IMAP4_SSL('imap.gmail.com')
        self.parent = parent
        self.database = Database()

    def login(self,email,password):
        data = self.connection.login(email,password)
        if data[0] == 'OK':
            return True
        else:
            return False

    def fetchMail(self):
        list = self.connection.list()[1]
        for folder in list:
            folder_data = folder.decode().split(' "/" ')
            if folder_data[1] == '"INBOX"':
                self.cache('inbox')
                self.fetch('inbox','INBOX')
            if folder_data[1] == '[Gmail]/Spam':
                self.fetch('[Gmail]/Spam')
            if folder_data[1] == '[Gmail]/Sent Mail':
                self.fetch('[Gmail]/Sent Mail')
            if folder_data[1] == '[Gmail]/Drafts':
                self.fetch('[Gmail]/Drafts')

    def fetch(self,folder,mail_folder):
        self.connection.select(mail_folder)
        result, data = self.connection.search(None, "ALL")
        ids = data[0]
        id_list = ids.split()
        synced_list = self.sync(folder,id_list)
        #@todo figure out threads
        for id in synced_list:
            result, data = self.connection.fetch(id, "(RFC822)")
            if result == 'OK':
                print(data)
                # email_message = email.message_from_string(data[0][1].decode())
                # print(email_message.items())

    def cache(self,folder):
        self.messages[folder] = self.database.getMessages(folder)

    def sync(self,folder,id_list):
        new_list = [];
        for id in id_list:
            if id.decode() not in self.messages[folder]:
               new_list.append(id)
        return new_list


