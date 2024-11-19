from .CellClass import Cell

class Board:
    def __init__(self, With : int, Hight : int):
        self.Board = []
        for i in range(With):
            help = []
            for j in range(Hight):
                help.append(Cell(Position=(i, j)))
            self.Board.append(help)
        for lines in self.Board:
            for point in lines:
                mass = []
                for i in range(-1, 2):
                    help = []
                    for j in range(-1, 2):
                        if (point.Position['x'] + i < 0 or point.Position['x'] + i > With - 1 or point.Position['y'] + j < 0 or point.Position['y'] + j > Hight - 1):
                            help.append(None)
                        else:
                            help.append(point)
                    mass.append(help)
                point.SetMyFriends(mass)
        print('sucsess')
