from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import QObject


class Cell(QPushButton):
	def __init__(self, Position=(0, 0)):
		super().__init__()
		self.Position = {'x': Position[0], 'y': Position[1]}
		self.amIDangerous = False
		self.MyFriends = []
		self.nearMe = 0
		self.Statuse = 'Close'

	def SetMyFriends(self, fr):
		for line in fr:
			help = []
			for point in line:
				if (point != self):
					help.append(point)
				else:
					help.append(None)
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

	def __str__(self):
		return {'Mines': '*' if self.amIDangerous else ' ' if self.nearMe == 0 else self.nearMe, 'Status': self.Statuse}
