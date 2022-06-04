from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont
from PyQt5 import QtCore

class Text:
    def __init__(
        self,
        window,
        text: str,
        font: str = 'Arial',
        color: str = '#000',
        fontSize = 14,
        x = 100,
        y = 100
        ):
        self.window = window
        self.text = text
        self.font = font
        self.color = color
        self.fontSize = fontSize
        self.position = position
        self.style = style
        self.x = x
        self.y = y
        self.position = QtCore.Qt.AlignLeft
        self.alignment = None


        self.label = QLabel(self.window.window)
        self.label.setText(self.text)
        self.label.setFont(QFont(self.font, self.fontSize))
        self.label.setStyleSheet(f'color: {self.color}')

        self.label.setAlignment(self.position)

        self.label.move(self.x, self.y)
