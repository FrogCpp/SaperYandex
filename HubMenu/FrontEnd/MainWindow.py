from PyQt6 import uic
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QMainWindow
import subprocess
import os

from Sql import SqlController


class MainWindowClass(QMainWindow):
    def __init__(self):
        super().__init__()
        a = '/'.join(os.path.dirname(__file__).split('\\'))
        uic.loadUi(f"{a}/MainWindow.ui", self)
        sp = lambda x : os.path.split(x)[0]
        self.way = '/'.join(sp(sp(os.path.dirname(__file__))).split('\\'))
        st = lambda : subprocess.run(["python", f'{self.way}/MainGame/mainGame.py'])
        self.StartButton.clicked.connect(st)
        self.CS = SqlController()
        ab = self.CS.drawTable(True)
        print(ab)
        self.first_v = [0, 0]
        self.second_v = [0, 0]
        self.ferd_v = [0, 0]

    def Refresh(self):
        self.first.setText(f"1:\ntime:{self.first_v[0]}, Date:{self.first_v[1]}")
        self.second.setText(f"1:\ntime:{self.second_v[0]}, Date:{self.second_v[1]}")
        self.ferd.setText(f"1:\ntime:{self.ferd_v[0]}, Date:{self.ferd_v[1]}")
