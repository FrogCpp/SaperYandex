import os.path

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow
from MainGame.SaperClasses.BoardClasses import Board


class Minesweeper(QMainWindow):
    def __init__(self, a: Board):
        self.a = a
        super().__init__()
        self.setWindowTitle("Sapper, Yandex!!!")
        self.Way = '/'.join(os.path.dirname(__file__).split('\\'))
        uic.loadUi(f"{self.Way}/minesweeper2.ui", self)
        self.board = {}
        self.init_ui(a)
        self.new_game_button.clicked.connect(self.close)
        self.statusBar().setStyleSheet("color: red;")
        self.game_board.setStyleSheet("border-color: black;\nborder-width: 2px;")

    def init_ui(self, a: Board):
        for i in range(a.Width):
            for j in range(a.Height):
                self.a.Board[i][j].setParent(self.game_board)
                self.a.Board[i][j].setFixedSize(50, 50)
                self.a.Board[i][j].move(50 * i, 50 * j)
                # self.board[i, j].setText(str(self.a.Board[i][j].__str__()["Mines"]))

    def dis_or_en_able_all(self, wtd=True):
        for i in self.a.Board:
            for j in i:
                j.setDisabled(True)
        self.statusBar().showMessage("YOU LOST" if wtd else "YOU VIN")
