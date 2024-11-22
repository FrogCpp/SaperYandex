import random

from .CellClass import Cell

class Board:
    def __init__(self, With : int, Hight : int, MineK : int):
        self.Board = []
        self.game = True
        for i in range(With):
            help = []
            for j in range(Hight):
                help.append(Cell(self, position=(i, j)))
            self.Board.append(help)

        for i in range(MineK):
            x = random.randint(0, With - 1)
            y = random.randint(0, Hight - 1)
            while self.Board[x][y].amIDangerous:
                x = random.randint(0, With-1)
                y = random.randint(0, Hight-1)
            self.Board[x][y].amIDangerous = True

        for lines in self.Board:
            for point in lines:
                mass = []
                for i in range(-1, 2):
                    help = []
                    for j in range(-1, 2):
                        x = point.Position['x'] + i
                        y = point.Position['y'] + j
                        if 0 <= x < With and 0 <= y < Hight:
                            help.append(self.Board[x][y])
                        else:
                            help.append(None)
                    mass.append(help)
                point.setMyFriends(mass)
        print('sucsess')

# for i in range(self.mine_amount):
# 			a = (randint(0, self.size_x - 1), randint(0, self.size_y - 1))
# 			if i == 0:
# 				mines.append(a)
# 			else:
# 				if a in mines:
# 					while a in mines:
# 						a = (randint(0, self.size_x - 1), randint(0, self.size_y - 1))
# 					mines.append(a)
# 				else:
# 					mines.append(a)
