import random

from MainGame.SaperClasses import Board
import sys
from MainGame.frontEND.front_end import Minesweeper
from PyQt6.QtWidgets import QApplication

app = QApplication(sys.argv)

a = Board(8, 8, random.randint(10, 10))

ex = Minesweeper(a)
a.DeadF = ex.dis_or_en_able_all
ex.show()
sys.exit(app.exec())
