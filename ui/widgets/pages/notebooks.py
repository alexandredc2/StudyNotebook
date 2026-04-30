from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSplitter,QFrame,QVBoxLayout,QHBoxLayout


class Notebooks(QSplitter):
    def __init__(self, parent=None):
        super().__init__(Qt.Horizontal, parent)
        self.setObjectName("Splitter_Functions")

        self._setup_notebooks_directories()
        self._setup_notebooks_area()
        self.setSizes([295, 800])

    def _setup_notebooks_directories(self):
        self.__notebooks_dir = QFrame()
        self.__notebooks_dir.setContentsMargins(10,2,10,20)
        self.__notebooks_dir.setObjectName("Frame_Buttons_Directories")
        self.__notebooks_dir.setMinimumWidth(295)
        self.__notebooks_dir.setMaximumWidth(350)
        layout = QVBoxLayout(self.__notebooks_dir)

        #...LAYOUT - SUPERIOR
        

        #...LAYOUT - INFERIOR

        #...LAYOUT - GERAL

        self.addWidget(self.__notebooks_dir)

    def _setup_notebooks_area(self):
        self.__notebooks_area = QFrame()
        self.__notebooks_area.setObjectName("Frame_Notebooks_Area")
        layout = QVBoxLayout(self.__notebooks_area)

        self.addWidget(self.__notebooks_area)