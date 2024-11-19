import random

class Cell():
    def __init__(self, Position=(0, 0)):
        self.Position = Position
        self.amIDangerous = random.randint(0, 100) % 2 == 0
        self.MyFriends = []
        self.nearMe = 0

    def SetMyFriends(self, fr):
        for i in fr:
            self.MyFriends.append(i)
            if (i.amIDangerious):
                self.nearMe += 1

    def ClickIvent(self):
        if (self.amIDangerous):
            return True