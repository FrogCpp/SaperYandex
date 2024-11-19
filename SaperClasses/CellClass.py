import random

class Cell:
    def __init__(self, Position=(0, 0), MineK=8):
        self.Position = {'x':Position[0], 'y':Position[1]}
        self.amIDangerous = random.randint(0, 100) % MineK == 0
        self.MyFriends = []
        self.nearMe = 0
        self.Statuse = 'Close'

    def SetMyFriends(self, fr):
        for line in fr:
            help = []
            for point in line:
                help.append(point)
                if (point is not None):
                    if (point.amIDangerous):
                        self.nearMe += 1
            self.MyFriends.append(help)

    def ClickIvent(self):
        self.Statuse = 'Open'
        if (self.amIDangerous):
            return True
        else:
            if (self.nearMe > 0):
                return False
            for i in self.MyFriends:
                for j in i:
                    try:
                        if (j.ClickIvent):
                            return True
                    except Exception:
                        pass
        return False

    def __str__(self):
        # return {'Mines':'*' if self.amIDangerous else '_' if self.nearMe == 0 else self.nearMe, 'Status':self.Statuse}
        return '*' if self.amIDangerous else '0' if self.nearMe == 0 else self.nearMe
