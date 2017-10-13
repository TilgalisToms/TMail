import sqlite3

class Database:

    configArray = {}

    def __init__(self):
        self.connect()
        self.checkAndCreateTables()
        # self.getConfig()

    def connect(self):
        self.db = sqlite3.connect('accounts.db')

    def checkAndCreateTables(self):
        self.connect()
        c = self.db.cursor()
        # c.execute('DROP TABLE `mailbox`')
        c.execute('CREATE TABLE IF NOT EXISTS `mailbox` (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `address` VARCHAR(255), `password` VARCHAR(255),`title` VARCHAR(255))')
        c.execute('CREATE TABLE IF NOT EXISTS `config` (`sid` varchar(32) PRIMARY KEY, `value` VARCHAR(255))')
        c.execute('CREATE TABLE IF NOT EXISTS `message` (`id` INTEGER PRIMARY KEY, `folder` VARCHAR(32), `html` TEXT, `sender` VARCHAR(255), `title` TEXT, `received` DATETIME, `read` INTEGER(1))')
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
        c.execute('INSERT INTO `mailbox` (`address`,`password`,`title`) VALUES (?,?,?)', (
            data['email'], data['password'], data['title'],
        ))
        self.db.commit()
        self.db.close()

    def saveAccount(self,id,data):
        self.connect()
        c = self.db.cursor()
        c.execute('UPDATE `mailbox` SET `address`=?, `password`=?, `title`=? WHERE `id`=?',(
            data['email'],data['password'],data['title'],id,
        ))
        self.db.commit()
        self.db.close()

    def getMessages(self,folder):
        self.connect()
        c = self.db.cursor()
        c.execute('SELECT * FROM `message` WHERE `folder`=?',(folder, ))
        array = {}
        results = c.fetchall()
        for result in results:
            item = {}
            item['id'] = result[0]
            item['html'] = result[2]
            item['sender'] = result[3]
            item['title'] = result[4]
            item['received'] = result[5]
            item['read'] = result[6] == 1
            array[result[0]] = item
        self.db.close()
        return array