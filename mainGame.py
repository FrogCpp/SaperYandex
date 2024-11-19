from SaperClasses import Board
import sys
from frontEND.front_end import Minesweeper
from PyQt6.QtWidgets import QApplication
a = Board(10, 10, 20)

app = QApplication(sys.argv)
ex = Minesweeper(a)
ex.show()
sys.exit(app.exec())
# тут пока ничего не трогаем
# тут будем писать, когда каждый свою часть напишет
