import sqlite3

class Database:

    def __init__(self):
        self.connect()
        self.checkAndCreateTables()

    def connect(self):
        self.db = sqlite3.connect('accounts.db')

    def checkAndCreateTables(self):
        self.connect()
        c = self.db.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS `mailbox` (`id` int primary key, `address` varchar(255), `password` varchar(255))')
        self.db.commit()
        self.db.close()

    def getMailboxes(self,full = False):
        self.connect()
        c = self.db.cursor()
        if full == True:
            c.execute('SELECT * FROM `mailbox` ORDER BY `id` ASC')
        else:
            c.execute('SELECT `address` FROM `mailbox` ORDER BY `id` ASC')

        results = c.fetchall()
        self.db.close()
        return results

