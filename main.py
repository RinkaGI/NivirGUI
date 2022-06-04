from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QWidget
import sys

class Window:
    def __init__(
        self,
        title: str,
        width: int = 800,
        height: int = 600,
        icon: str = '',
        bgcolor: str = '#FFF'
    ) -> None:
        self.title = title
        self.width = width
        self.height = height
        self.icon = icon
        self.bgcolor = bgcolor

        self.application = QApplication(sys.argv)
        self.window = QWidget()

        self.window.setWindowTitle(self.title)
        self.window.setGeometry(0, 0, self.width, self.height)
        self.window.setStyleSheet(f'background-color: {bgcolor}')

        if icon != '':
            self.window.setWindowIcon(QtGui.QIcon(self.icon))
        else:
            pass

    def run(self):
        self.window.show()
        sys.exit(self.application.exec_())
