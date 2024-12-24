import sqlite3
from datetime import datetime

class SqlController:
    def __init__(self):
        self.con = sqlite3.connect("TimeDataBase")
        self.cur = self.con.cursor()
        comm1 = """CREATE TABLE IF NOT EXISTS bestTime (ID INTEGER PRIMARY KEY, time REAL, date TEXT)"""
        comm2 = """CREATE TABLE IF NOT EXISTS bestTimeAll (ID INTEGER PRIMARY KEY, time REAL, date TEXT)"""
        self.cur.execute(comm1)
        self.con.commit()
        self.cur.execute(comm2)
        self.con.commit()

    def end(self):
        self.con.close()

    def drawTable(self, rt = False):
        result = self.cur.execute("""SELECT name FROM sqlite_master WHERE TYPE = 'table'""").fetchall()
        mass = {}
        for elem in result:
            sql = f"""SELECT * FROM {elem[0]}"""
            res = self.cur.execute(sql).fetchall()
            if not rt:
                print(elem[0])
                print(res)
            else:
                mass[elem[0]] = res
        return mass

    def Add(self, timee : float):
        a = True
        for i in self.drawTable(True)['bestTime']:
            if i[2] == datetime.now().strftime('%d.%m.%Y'):
                self.Change(i[0], time.time() - self.startTime)
                a = False
                break
        if a:
            sql = f"""INSERT INTO bestTime (time, date) VALUES ({round(timee, 3)}, '{datetime.now().strftime('%d.%m.%Y')}')"""
            sql1 = f"""INSERT INTO bestTimeAll (time, date) VALUES ({round(timee, 3)}, '{datetime.now().strftime('%d.%m.%Y')}')"""
            self.cur.execute(sql)
            self.con.commit()
            self.cur.execute(sql1)
            self.con.commit()

    def Delet(self, ID):
        sql = f"""DELETE FROM bestTime WHERE ID = {ID}"""
        self.cur.execute(sql)
        self.con.commit()

    def Change(self, ID, value):
        sql = f"""UPDATE bestTime SET time = {value} WHERE id = {ID}"""
        self.cur.execute(sql)
        self.con.commit()
