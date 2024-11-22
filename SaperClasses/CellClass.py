from PyQt6.QtWidgets import QPushButton, QApplication
from PyQt6.uic.Compiler.qtproxies import QtCore
from PyQt6.QtCore import Qt


class Cell(QPushButton):
	def __init__(self, brd, position=(0, 0)):
		super().__init__()
		self.Position = {'x': position[0], 'y': position[1]}
		self.amIDangerous = False
		self.MyFriends = []
		self.nearMe = 0
		self.Statuse = 'Close'
		self.MyBoard = brd
		self.flag = False
		self.clicked.connect(self.ClickIvent)
		self.setStyleSheet("border-image: url(Textures/MineSweeper_ModeliveskyCom/128x128/unknown_1_128x128.png);")

	def setMyFriends(self, fr):
		for line in fr:
			help = []
			for point in line:
				if point != self:
					help.append(point)
				else:
					help.append(None)
				if point is not None:
					if point.amIDangerous:
						self.nearMe += 1
			self.MyFriends.append(help)

	def SetFlag(self):
		self.flag = not self.flag
		print('aboba')

	def ClickIvent(self):
		if QApplication.mouseButtons() & Qt.MouseButton.RightButton:
			self.SetFlag()
			return 0
		self.setStyleSheet(f"border-image: url({str(self.__str__()["Mines"] if not self.flag else self.__str__())});")
		if self.Statuse != 'Close':
			return False
		self.Statuse = 'Open'
		if self.amIDangerous:
			self.MyBoard.DeadF()
			return True
		else:
			if self.nearMe > 0:
				return False
			for i in self.MyFriends:
				for j in i:
					try:
						if j.ClickIvent():
							self.MyBoard.DeadF()
							return True
					except Exception:
						pass
		return False

	def __str__(self):
		return {'Mines': 'Textures/MineSweeper_ModeliveskyCom/64x64/bebebe.png' if self.amIDangerous else f"Textures/MineSweeper_ModeliveskyCom/64x64/{self.nearMe}.png" if self.nearMe != 0 else "Textures/MineSweeper_ModeliveskyCom/128x128/empty_128x128.png", 'Status': self.Statuse} if not self.flag else "Textures/MineSweeper_ModeliveskyCom/128x128/flat_1_128x128.png"
