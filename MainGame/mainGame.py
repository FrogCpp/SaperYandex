from MainGame.SaperClasses import Board
import sys
from MainGame.frontEND.front_end import Minesweeper
from PyQt6.QtWidgets import QApplication

app = QApplication(sys.argv)
properties = []
with open("prop.txt", 'r') as file:
	line = file.read().split()
	line = [int(el) for el in line]
	properties = line
board = Board(properties[0], properties[1], properties[2])


ex = Minesweeper(board)
board.DeadF = ex.dis_or_en_able_all
ex.show()
sys.exit(app.exec())
