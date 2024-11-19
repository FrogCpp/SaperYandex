import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton


class Minesweeper(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("minesweeper.ui", self)
        self.init_ui()
        self.board = []

    def init_ui(self):
        for i in range(10):
            for j in range(10):
                self.board[i][j] = QPushButton(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Minesweeper()
    ex.show()
    sys.exit(app.exec())
