from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow


class MainWindowClass(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./HubMenu/FrontEnd/MainWindow.ui", self)