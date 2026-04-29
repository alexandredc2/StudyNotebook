from PyQt5.QtWidgets import QFrame, QVBoxLayout, QStackedWidget
from assets.style import central_style


class CentralArea(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Frame_Central_Area")
        self.setStyleSheet(central_style())

