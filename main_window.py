from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configurando o layout basico
        self.cWidget = QWidget()
        self.vLayout = QVBoxLayout()

        self.cWidget.setLayout(self.vLayout)
        self.setCentralWidget(self.cWidget)

        # Adicionando o itulo da janela
        self.setWindowTitle('Calculadora')

    def ajustFixedSize(self):
        # Ajustando o tamanho e fixando ele
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)

    def makeMsgBox(self):
        return QMessageBox(self)
