from Assets.SaperClasses import Board
import sys
from Assets.frontEND.front_end import Minesweeper
from PyQt6.QtWidgets import QApplication

app = QApplication(sys.argv)

a = Board(10, 10, 20)

ex = Minesweeper(a)
a.DeadF = ex.disable_all
ex.show()
sys.exit(app.exec())
