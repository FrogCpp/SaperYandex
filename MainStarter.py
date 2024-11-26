from HubMenu import MainWindowClass
import sys
from PyQt6.QtWidgets import QApplication
from MainGame import mainGame

app = QApplication(sys.argv)

ex = MainWindowClass(mainGame)
ex.show()
sys.exit(app.exec())
