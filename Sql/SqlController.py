import sqlite3
from datetime import datetime

class SqlController:
    def __init__(self):
        self.con = sqlite3.connect("TimeDataBase")
        self.cur = self.con.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS bestTime (ID INTEGER PRIMARY KEY, time REAL, date TEXT)""")
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
        sql = f"""INSERT INTO bestTime (time, date) VALUES ({timee}, '{datetime.now().strftime('%d.%m.%Y')}')"""
        self.cur.execute(sql)
        self.con.commit()

    def Delet(self, ID):
        sql = f"""DELETE FROM bestTime WHERE ID = {ID}"""
        self.cur.execute(sql)
        self.con.commit()
