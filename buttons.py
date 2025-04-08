from typing import TYPE_CHECKING

import math
from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget
from PySide6.QtCore import Slot
from enviroments import BIG_FONT_SIZE
from util import isEmpty, isNumOrDot, isValidNumber

if TYPE_CHECKING:
    from display import Display
    from main_window import MainWindow
    from info import Info


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}')
        self.setMinimumSize(75, 75)


class ButtonsGrid(QGridLayout):
    def __init__(
            self,
            display: 'Display',
            info: 'Info',
            window: 'MainWindow',
            parent: QWidget | None = None,
    ):
        super().__init__(parent)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N',  '0', '.', '='],
        ]
        self._display = display
        self._info = info
        self._window = window
        self._equation = ''
        self._defaultEquation = 'Sua conta'
        self._left = None
        self._right = None
        self._op = None
        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self._info.setText(value)

    def _makeGrid(self):
        self._display.eqPressed.connect(self._eq)
        self._display.delPressed.connect(self._display.backspace)
        self._display.clearPressed.connect(self._clear)
        self._display.inputPressed.connect(self._insertTextToDisplay)
        self._display.opPressed.connect(self._configLeftOperator)

        for rowNumber, rowData in enumerate(self._gridMask):
            for columnNumber, buttonText in enumerate(rowData):
                button = Button(buttonText)

                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                self.addWidget(button, rowNumber, columnNumber)
                buttonSlot = self._makeSlot(
                    self._insertTextToDisplay,
                    button.text()
                )
                self._connectButtonClicked(button, buttonSlot)

    def _connectButtonClicked(self, button: Button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button: Button):
        text = button.text()

        if text == 'C':
            self._connectButtonClicked(button, self._clear)

        if text == '◀':
            self._connectButtonClicked(button, self._display.backspace)

        if text == 'N':
            self._connectButtonClicked(button, self._invertNumber)

        if text in '+-*/^':
            self._connectButtonClicked(
                button,
                self._makeSlot(self._configLeftOperator, text)
            )

        if text == '=':
            self._connectButtonClicked(button, self._eq)

    @Slot()
    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool, )
        def realSlot():
            func(*args, **kwargs)
        return realSlot

    @Slot()
    def _invertNumber(self):
        displayText = self._display.text()

        if not isValidNumber(displayText):
            return

        newNumber = -float(displayText)
        self._display.setText(str(newNumber))

    @Slot()
    def _insertTextToDisplay(self, text: str):
        newDisplayValue = self._display.text() + text

        if not isValidNumber(newDisplayValue):
            return

        self._display.insert(text)

    @Slot()
    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._defaultEquation
        self._display.clear()

    @Slot()
    def _configLeftOperator(self, text):
        displayText = self._display.text()
        self._display.clear()

        if not isValidNumber(displayText) and self._left is None:
            self._showError('Você nao digitou nada')
            return

        if self._left is None:
            self._left = float(displayText)

        self._op = text
        self.equation = f'{self._left} {self._op} '

    @Slot()
    def _eq(self):
        displayText = self._display.text()

        if not isValidNumber(displayText) or self._left is None:
            return

        self._right = float(displayText)
        self.equation = f'{self._left} {self._op} {self._right}'
        result = 'error'

        try:
            if '^' in self.equation and isinstance(self._left, float):
                result = math.pow(self._left, self._right)  # type: ignore
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self._showError('Zero division error')
        except OverflowError:
            self._showError('Numero muito grande')

        self._info.setText(f'{self.equation} = {result}')
        self._left = result
        self._right = None

        if result == 'error':
            self._left = None

    def _showError(self, text):
        msgBox = self._window.makeMsgBox()
        msgBox.setText(text)
        msgBox.setIcon(msgBox.Icon.Warning)
        msgBox.exec()
