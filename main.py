import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from PySide6.QtGui import QIcon
from enviroments import WINDOW_ICON_PATH
from display import Display
from info import Info
from buttons import ButtonsGrid
from style import setupTheme


if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()

    # Definindo o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    app.setWindowIcon(icon)
    window.setWindowIcon(icon)
    if sys.platform.startswith('win'):
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            u'CompanyName.ProductName.SubProduct.VersionInformation')

    # Info
    info = Info('Sua conta')
    window.addWidgetToVLayout(info)

    # Criando o display
    display = Display()
    window.addWidgetToVLayout(display)

    # Criando a grid de botões
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Executa tudo
    window.ajustFixedSize()
    window.show()
    app.exec()
