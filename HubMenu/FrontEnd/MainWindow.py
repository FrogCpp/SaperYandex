from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow
import subprocess
import os

class MainWindowClass(QMainWindow):
    def __init__(self):
        super().__init__()
        a = '/'.join(os.path.dirname(__file__).split('\\'))
        uic.loadUi(f"{a}/MainWindow.ui", self)
        sp = lambda x : os.path.split(x)[0]
        self.way = '/'.join(sp(sp(os.path.dirname(__file__))).split('\\'))
        st = lambda : subprocess.run(["python", f'{self.way}/MainGame/mainGame.py'])
        self.StartButton.clicked.connect(st)