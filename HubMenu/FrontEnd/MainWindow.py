from PyQt6 import uic
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QSizePolicy
from PyQt6.QtWidgets import QFileDialog

import subprocess
import os

from Sql import SqlController


class MainWindowClass(QMainWindow):
    def __init__(self):
        super().__init__()
        with open("prop.txt", "w") as prop_file:
            prop_file.write("8 8 10")
        self.game_width = 0
        self.game_height = 0
        self.game_mines = 0
        self.setWindowTitle("Sapper, Yandex!!!")
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.setFixedSize(500, 300)
        self.setMaximumSize(500, 300)
        a = '/'.join(os.path.dirname(__file__).split('\\'))
        uic.loadUi(f"{a}/MainWindow.ui", self)
        self.way = '/'.join(self.splt(self.splt(os.path.dirname(__file__))).split('\\'))
        self.StartButton.clicked.connect(self.start_game)
        self.saveButton.clicked.connect(self.save_conf)
        self.openButton.clicked.connect(self.open_conf)
        self.CS = SqlController()
        self.first_v = [0, 0]
        self.second_v = [0, 0]
        self.ferd_v = [0, 0]
        self.forth_v = [0, 0]
        self.fifth_v = [0, 0]
        self.widthBox.valueChanged.connect(self.update_properties)
        self.widthBox.valueChanged.connect(self.update_properties)
        self.widthBox.valueChanged.connect(self.update_properties)

        self.Refresh()

    def start_game(self):
        subprocess.run(["python3", f'{self.way}/MainGame/mainGame.py'])

    def save_conf(self):
        save_file = QFileDialog.getSaveFileName(self, "Save properties file")
        try:
            with open(save_file[0], "w") as save_f, open(f"{self.way}/prop.txt", 'r') as read_file:
                save_f.write(read_file.read())
        except FileNotFoundError:
            pass

    def open_conf(self):
        open_file = QFileDialog.getOpenFileName(self, "Open properties file")[0]
        properties = []
        try:
            with open(open_file, "r") as open_f:
                temp = [int(el) for el in open_f.read().split()]
                properties = temp
        except FileNotFoundError:
            return
        self.widthBox.setValue(properties[0])
        self.heightBox.setValue(properties[1])
        self.mineBox.setValue(properties[2])
        self.update_properties()

    def splt(self, x):
        return os.path.split(x)[0]

    def update_properties(self):
        self.game_width = self.widthBox.value()
        self.game_height = self.heightBox.value()
        self.game_mines = self.mineBox.value()
        with open("prop.txt", 'w') as file:
            file.write(' '.join([str(el) for el in [self.game_width, self.game_height, self.game_mines]]))

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

        ab = list(sorted(map(lambda x: (int(x[1]), x[2], x[0]), self.CS.drawTable(True)['bestTime'])))
        for i in ab[5:]:
            self.CS.Delet(i[2])
