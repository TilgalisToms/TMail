import sqlite3

class Database:

    configArray = []

    def __init__(self):
        self.connect()
        self.checkAndCreateTables()
        self.getConfig()

    def connect(self):
        self.db = sqlite3.connect('accounts.db')

    def checkAndCreateTables(self):
        self.connect()
        c = self.db.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS `mailbox` (`id` int primary key, `address` varchar(255), `password` varchar(255))')
        c.execute('CREATE TABLE IF NOT EXISTS `config` (`sid` varchar(32) primary key, `value` varchar(255))')
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

    def getConfig(self):
        self.connect()
        c = self.db.cursor()
        c.execute('SELECT * FROM `config`')
        self.configArray = c.fetchall()
        self.db.close()

    def getConfigValue(self, sid):
        for item in self.configArray:
            if item[0] == sid:
                return item[1]
            else:
                return False

    def setConfigValue(self, sid, value):
        self.connect()
        c = self.db.cursor()
        exists = c.execute('SELECT `value` FROM `config` WHERE `sid`=?',(sid,)).fetchone()
        if exists != None:
            c.execute('UPDATE `config` SET `value`=? WHERE `sid`=?', (value, sid,))
        else:
            c.execute('INSERT OR IGNORE INTO `config` VALUES (?,?)',(sid,value,))
        self.db.commit()
        self.db.close()
        for item in self.configArray:
            if item[0] == sid:
                item[1] = value