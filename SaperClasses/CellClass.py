from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import QObject
from BoardClasses import Board


class Cell(QPushButton):
	def __init__(self, brd: Board, Position=(0, 0)):
		super().__init__()
		self.Position = {'x': Position[0], 'y': Position[1]}
		self.amIDangerous = False
		self.MyFriends = []
		self.nearMe = 0
		self.Statuse = 'Close'
		self.MyBoard = brd

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
			self.MyBoard.game = False
			return True
		else:
			if (self.nearMe > 0):
				return False
			for i in self.MyFriends:
				try:
					if (i.ClickIvent):
						self.MyBoard.game = False
						return True
				except Exception:
					pass
		return False

	def __str__(self):
		return {'Mines': '*' if self.amIDangerous else ' ' if self.nearMe == 0 else self.nearMe, 'Status': self.Statuse}
