from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QSplitter, QVBoxLayout


class Pendencias(QSplitter):
    def __init__(self, parent=None):
        super().__init__(Qt.Horizontal, parent)
        self.setObjectName("Splitter_Functions")

        self._setup_pendencias_directories()
        self._setup_pendencias_area()
        self.setSizes([240, 800])

    def _setup_pendencias_directories(self):
        self.__pendencias_dir = QFrame()
        self.__pendencias_dir.setObjectName("Frame_Buttons_Directories")
        self.__pendencias_dir.setMinimumWidth(240)
        self.__pendencias_dir.setMaximumWidth(350)
        layout = QVBoxLayout(self.__pendencias_dir)

        self.addWidget(self.__pendencias_dir)

    def _setup_pendencias_area(self):
        self.__pendencias_area = QFrame()
        self.__pendencias_area.setObjectName("Frame_Pendencias_Area")
        layout = QVBoxLayout(self.__pendencias_area)

        self.addWidget(self.__pendencias_area)