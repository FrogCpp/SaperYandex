from SaperClasses import Board
import sys
from frontEND.front_end import Minesweeper
from PyQt6.QtWidgets import QApplication

app = QApplication(sys.argv)

a = Board(10, 10, 20)
a.create()

ex = Minesweeper(a)
a.DeadF = ex.dis_or_en_able_all
ex.show()
sys.exit(app.exec())
