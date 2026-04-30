from PyQt5.QtWidgets import QVBoxLayout, QStackedWidget
from assets.style import central_style
from ui.widgets.pages.brainstorms import Brainstorms
from ui.widgets.pages.homepage import Homepage
from ui.widgets.pages.languages import Languages
from ui.widgets.pages.notebooks import Notebooks
from ui.widgets.pages.pendencias import Pendencias


class CentralArea(QStackedWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Frame_Central_Area")
        self.setStyleSheet(central_style())

        self.addWidget(Homepage())
        self.addWidget(Notebooks())
        self.addWidget(Pendencias())
        self.addWidget(Brainstorms())
        self.addWidget(Languages())

