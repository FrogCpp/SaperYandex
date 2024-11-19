from SaperClasses import Board
import sys
from frontEND.front_end import Minesweeper
from PyQt6.QtWidgets import QApplication

app = QApplication(sys.argv)

a = Board(10, 10, 20)

ex = Minesweeper(a)
ex.show()
sys.exit(app.exec())
# тут пока ничего не трогаем
# тут будем писать, когда каждый свою часть напишет
