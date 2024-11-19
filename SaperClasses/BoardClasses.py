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
                        try:
                            help.append(self.Board[point.Position[0] + i][point.Position[1] + j])
                        except Exception:
                            help.append(None)
                    mass.append(help)
                point.SetMyFriends(mass)
