from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QWidget
from enviroments import SMALL_FONT_SIZE


class Info(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None):
        super().__init__(text, parent)

        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
