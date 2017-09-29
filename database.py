import sqlite3

class Database:

    def __init__(self):
        self.db = sqlite3.connect('accounts.db')
        self.checkAndCreateTables()

    def checkAndCreateTables(self):
        c = self.db.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS `mailbox` (`id` int primary key, `address` varchar(255), `password` varchar(255))')
        #SEED
        c.execute('INSERT INTO `mailbox` VALUES(1,"foo@bar.com","forshaparole")')

    def getMailboxes(self):
        c = self.db.cursor()
        c.execute('SELECT `address` FROM `mailbox` ORDER BY `id` ASC')
        return c.fetchall()
