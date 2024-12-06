import random
import time

from Sql import SqlController
from .CellClass import Cell


class Board:
    def __init__(self, Width: int, Height: int, MineK: int):
        self.startTime = time.time()
        self.Board = []
        self.DeadF = 0
        self.Width = Width
        self.Height = Height
        self.SC = SqlController()
        for i in range(self.Width):
            help = []
            for j in range(self.Height):
                help.append(Cell(self, position=(i, j)))
            self.Board.append(help)

        self.MakeMines(MineK)

        for lines in self.Board:
            for point in lines:
                mass = []
                for i in range(-1, 2):
                    help = []
                    for j in range(-1, 2):
                        x = point.Position['x'] + i
                        y = point.Position['y'] + j
                        if 0 <= x < self.Width and 0 <= y < self.Height:
                            help.append(self.Board[x][y])
                        else:
                            help.append(None)
                    mass.append(help)
                point.setMyFriends(mass)

    def MakeMines(self, MineK):
        for i in range(MineK):
            x = random.randint(0, self.Width - 1)
            y = random.randint(0, self.Height - 1)
            while self.Board[x][y].amIDangerous:
                x = random.randint(0, self.Width - 1)
                y = random.randint(0, self.Height - 1)
            self.Board[x][y].amIDangerous = True

    def CheckWin(self):
        a = self.Width * self.Height
        for line in self.Board:
            for point in line:
                if point.amIDangerous and point.flag:
                    a -= 1
                elif not point.amIDangerous and point.Statuse != "Close":
                    a -= 1
        if a == 0:
            self.DeadF(False)
            self.SC.Add(time.time() - self.startTime)
