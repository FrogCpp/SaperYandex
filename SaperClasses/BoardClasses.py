from .CellClass import Cell

class Board:
    def __init__(self, With : int, Hight : int, MineK : int):
        self.Board = []
        for i in range(With):
            help = []
            for j in range(Hight):
                help.append(Cell(Position=(i, j, MineK)))
            self.Board.append(help)
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
                point.SetMyFriends(mass)
        print('sucsess')
