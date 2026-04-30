from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QMainWindow, QFrame, QHBoxLayout

from ui.widgets.central import CentralArea
from ui.widgets.directories import Directories
from ui.widgets.menubar import MenuBar

#Constantes
MIN_WIDTH = 1490
MIN_HEIGHT = 860

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(MIN_WIDTH,MIN_HEIGHT))
        self.setWindowFlags(Qt.FramelessWindowHint)

        self._config_menubar()
        self._config_central_area()

    def _config_menubar(self):
        self.__menubar = MenuBar()
        self.setMenuBar(self.__menubar)


    def _config_central_area(self):
        container = QFrame()
        layout = QHBoxLayout(container)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)

        self.__directories = Directories()
        self.__directories.setFixedWidth(240)
        layout.addWidget(self.__directories)

        self.__central_area = CentralArea()
        layout.addWidget(self.__central_area, stretch=1)

        self.__directories.view_changed.connect(self.__central_area.setCurrentIndex)

        self.setCentralWidget(container)




