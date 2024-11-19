import random

class Cell:
    def __init__(self, Position=(0, 0)):
        self.Position = Position
        self.amIDangerous = random.randint(0, 100) % 2 == 0
        self.MyFriends = []
        self.nearMe = 0
        self.Statuse = 'Close'

    def SetMyFriends(self, fr):
        for line in fr:
            for point in line:
                if (point != self):
                    self.MyFriends.append(point)
                else:
                    self.MyFriends.append(None)
                if (point is not None):
                    if (point.amIDangerous):
                        self.nearMe += 1

    def ClickIvent(self):
        self.Statuse = 'Open'
        if (self.amIDangerous):
            return True
        else:
            if (self.nearMe > 0):
                return False
            for i in self.MyFriends:
                try:
                    if (i.ClickIvent):
                        return True
                except Exception:
                    pass
        return False
