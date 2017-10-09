import sqlite3

class Database:

    configArray = {}

    def __init__(self):
        self.connect()
        self.checkAndCreateTables()
        self.getConfig()

    def connect(self):
        self.db = sqlite3.connect('accounts.db')

    def checkAndCreateTables(self):
        self.connect()
        c = self.db.cursor()
        # c.execute('DROP TABLE `mailbox`')
        c.execute('CREATE TABLE IF NOT EXISTS `mailbox` (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `address` varchar(255), `password` varchar(255),`imap` varchar(255),`smtp` varchar(255),`title` varchar(255))')
        c.execute('CREATE TABLE IF NOT EXISTS `config` (`sid` varchar(32) PRIMARY KEY, `value` varchar(255))')
        self.db.commit()
        self.db.close()

    def getMailboxes(self):
        self.connect()
        c = self.db.cursor()
        c.execute('SELECT * FROM `mailbox` ORDER BY `id` ASC')
        results = c.fetchall()

        array = {}
        for result in results:
            row = {
                'id': result[0],
                'address': result[1],
                'password': result[2],
                'imap': result[3],
                'smtp': result[4],
                'title': result[5]
            }
            array[result[0]] = row

        self.db.close()
        return array

    def getMailbox(self,id):
        self.connect()
        c = self.db.cursor()
        c.execute('SELECT * FROM `mailbox` WHERE `id`=?',(id, ))
        results = c.fetchone()
        array = {
            'id':results[0],
            'address':results[1],
            'password':results[2],
            'imap':results[3],
            'smtp':results[4],
            'title':results[5]
        }
        self.db.close()
        return array

    def getConfig(self):
        self.connect()
        c = self.db.cursor()
        c.execute('SELECT * FROM `config`')
        configArray = c.fetchall()
        for item in configArray:
            self.configArray[item[0]] = item[1]
        self.db.close()

    def getConfigValue(self, sid):
        if self.configArray[sid] != None:
            return self.configArray[sid]
        else:
            return False

    def setConfigValue(self, sid, value):
        self.connect()
        c = self.db.cursor()
        if self.configArray[sid] != None:
            c.execute('UPDATE `config` SET `value`=? WHERE `sid`=?', (value, sid,))
        else:
            c.execute('INSERT OR IGNORE INTO `config` VALUES (?,?)',(sid,value,))
        self.db.commit()
        self.db.close()
        self.configArray[sid] = value

    def removeMailbox(self,id):
        self.connect()
        c = self.db.cursor()
        c.execute('DELETE FROM `mailbox` WHERE `id`=?',(id,))
        self.db.commit()
        self.db.close()

    def createAccount(self,data):
        self.connect()
        c = self.db.cursor()
        c.execute('INSERT INTO `mailbox` (`address`,`password`,`imap`,`smtp`,`title`) VALUES (?,?,?,?,?)', (
            data['email'], data['password'], data['imap'], data['smtp'], data['title'],
        ))
        self.db.commit()
        self.db.close()

    def saveAccount(self,id,data):
        self.connect()
        c = self.db.cursor()
        c.execute('UPDATE `mailbox` SET `address`=?, `password`=?, `imap`=?, `smtp`=?, `title`=? WHERE `id`=?',(
            data['email'],data['password'],data['imap'],data['smtp'],data['title'],id,
        ))
        self.db.commit()
        self.db.close()