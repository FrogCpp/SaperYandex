from HubMenu import MainWindowClass
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6 import QtCore

app = QApplication(sys.argv)


def update():
    ex.Refresh()


timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.setInterval(1000)
timer.start()

ex = MainWindowClass()
ex.show()
sys.exit(app.exec())

# python -m PyInstaller MainStarter.spec
