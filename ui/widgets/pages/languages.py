from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSplitter, QFrame, QVBoxLayout, QPushButton


class Languages(QSplitter):
    def __init__(self, parent=None):
        super().__init__(Qt.Horizontal, parent)
        self.setObjectName("Splitter_Functions")

        self._setup_languages_directories()
        self._setup_languages_area()
        self.setSizes([240,800])

    def _setup_languages_directories(self):
        self.__languages_dir = QFrame()
        self.__languages_dir.setObjectName("Frame_Buttons_Directories")
        self.__languages_dir.setMinimumWidth(240)
        self.__languages_dir.setMaximumWidth(350)
        layout = QVBoxLayout(self.__languages_dir)



        self.addWidget(self.__languages_dir)

    def _setup_languages_area(self):
        self.__languages_area = QFrame()
        self.__languages_area.setObjectName("Frame_Languages_Area")
        layout = QVBoxLayout(self.__languages_area)



        self.addWidget(self.__languages_area)

