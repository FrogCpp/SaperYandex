from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QPushButton, QMainWindow
from SaperClasses.BoardClasses import Board


class Minesweeper(QMainWindow):
    def __init__(self, a: Board):
        self.a = a
        super().__init__()
        uic.loadUi("./frontEND/minesweeper.ui", self)
        self.board = {}
        self.init_ui()
        self.on_pushbuttons_clicked()

    def init_ui(self):
        for i in range(10):
            for j in range(10):
                self.a.Board[i][j].setParent(self.game_board)
                self.a.Board[i][j].setFixedSize(50, 50)
                self.a.Board[i][j].move(49 * i, 40 * j)
                # self.board[i, j].setText(str(self.a.Board[i][j].__str__()["Mines"]))

    def disable_all(self):
        for i in self.a.Board:
            for j in i:
                j.setDisabled(True)
        self.statusBar().setStyleSheet("color: red")
        self.statusBar().showMessage("YOU = LOH")

    def on_pushbuttons_clicked(self):
        for i in self.a.Board:
            for j in i:
                j.clicked.connect(j.ClickIvent)
