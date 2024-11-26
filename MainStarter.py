from HubMenu import MainWindowClass
import sys
from PyQt6.QtWidgets import QApplication

app = QApplication(sys.argv)

ex = MainWindowClass()
ex.show()
sys.exit(app.exec())

# python -m PyInstaller MainStarter.spec
