from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow
import os
#
# def start():
#     os.startfile("../../MainGame/mainGame.py")

class MainWindowClass(QMainWindow):
    def __init__(self, start):
        super().__init__()
        uic.loadUi("./HubMenu/FrontEnd/MainWindow.ui", self)
        Start = lambda: os.startfile(start)
        self.StartButton.clicked.connect(start)