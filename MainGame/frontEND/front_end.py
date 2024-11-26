import os.path

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow
from MainGame.SaperClasses.BoardClasses import Board


class Minesweeper(QMainWindow):
    def __init__(self, a: Board):
        self.a = a
        super().__init__()
        self.Way = '/'.join(os.path.dirname(__file__).split('\\'))
        uic.loadUi(f"{self.Way}/minesweeper2.ui", self)
        self.board = {}
        self.init_ui()
        self.new_game_button.clicked.connect(self.EndGame)
        self.statusBar().setStyleSheet("color: red")

    def init_ui(self):
        for i in range(10):
            for j in range(10):
                self.a.Board[i][j].setParent(self.game_board)
                self.a.Board[i][j].setFixedSize(50, 50)
                self.a.Board[i][j].move(49 * i, 40 * j)
                # self.board[i, j].setText(str(self.a.Board[i][j].__str__()["Mines"]))

    def dis_or_en_able_all(self, wtd: bool):
        for i in self.a.Board:
            for j in i:
                if wtd == False:
                    j.Statuse = 'Close'
                    j.setStyleSheet("border-image: url(Textures/MineSweeper_ModeliveskyCom/128x128/unknown_1_128x128.png);")
                j.setDisabled(wtd)
        self.statusBar().showMessage("YOU = LOH" if wtd else "")

    def EndGame(self):
        self.close()