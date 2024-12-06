from PyQt6 import uic
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QSizePolicy

import subprocess
import os

from Sql import SqlController


class MainWindowClass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sapper, Yandex!!!")
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.setFixedSize(500, 300)
        self.setMaximumSize(500, 300)
        a = '/'.join(os.path.dirname(__file__).split('\\'))
        uic.loadUi(f"{a}/MainWindow.ui", self)
        sp = lambda x: os.path.split(x)[0]
        self.way = '/'.join(sp(sp(os.path.dirname(__file__))).split('\\'))
        st = lambda: subprocess.run(["python", f'{self.way}/MainGame/mainGame.py'])
        self.StartButton.clicked.connect(st)
        self.CS = SqlController()
        self.first_v = [0, 0]
        self.second_v = [0, 0]
        self.ferd_v = [0, 0]
        self.forth_v = [0, 0]
        self.fifth_v = [0, 0]
        self.Refresh()

    def Refresh(self):
        ab = list(sorted(map(lambda x: (x[1], x[2]), self.CS.drawTable(True)['bestTime'])))
        self.first_v = ab[0] if len(ab) > 0 else ['None', 'None']
        self.second_v = ab[1] if len(ab) > 1 else ['None', 'None']
        self.ferd_v = ab[2] if len(ab) > 2 else ['None', 'None']
        self.forth_v = ab[3] if len(ab) > 3 else ['None', 'None']
        self.fifth_v = ab[4] if len(ab) > 4 else ['None', 'None']
        self.first.setText(f"1:\ntime:{self.first_v[0]} s, {self.first_v[1]}")
        self.second.setText(f"2:\ntime:{self.second_v[0]} s, {self.second_v[1]}")
        self.ferd.setText(f"3:\ntime:{self.ferd_v[0]} s, {self.ferd_v[1]}")
        self.forth.setText(f"4:\ntime:{self.forth_v[0]} s, {self.forth_v[1]}")
        self.fifth.setText(f"5:\ntime:{self.fifth_v[0]} s, {self.fifth_v[1]}")

        self.CS.drawTable()

        ab = list(sorted(map(lambda x: (int(x[1]), x[2], x[0]), self.CS.drawTable(True)['bestTime'])))
        for i in ab[5:]:
            self.CS.Delet(i[2])
