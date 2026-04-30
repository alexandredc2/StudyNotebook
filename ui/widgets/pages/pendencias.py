from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFrame, QSplitter, QVBoxLayout, QHBoxLayout,QPushButton


class Pendencias(QSplitter):
    def __init__(self, parent=None):
        super().__init__(Qt.Horizontal, parent)
        self.setObjectName("Splitter_Functions")

        self._setup_pendencias_directories()
        self._setup_pendencias_area()
        self.setSizes([295, 800])

    def _setup_pendencias_directories(self):
        self.__pendencias_dir = QFrame()
        self.__pendencias_dir.setContentsMargins(10,2,10,20)
        self.__pendencias_dir.setObjectName("Frame_Buttons_Directories")
        self.__pendencias_dir.setMinimumWidth(295)
        self.__pendencias_dir.setMaximumWidth(350)
        layout = QVBoxLayout(self.__pendencias_dir)

        #...LAYOUT - SUPERIOR
        container_btns = QFrame()
        layout_btns = QHBoxLayout(container_btns)
        self.__btn_pendencias_new_folder = QPushButton("  Nova Pasta")
        self.__btn_pendencias_new_folder.setCursor(Qt.PointingHandCursor)
        self.__btn_pendencias_new_folder.setIcon(QIcon("assets/icon_newfolder.png"))
        self.__btn_pendencias_new_folder.setObjectName("Buttons_Functions_Directories")
        self.__btn_pendencias_new_file = QPushButton("  Novo Arquivo")
        self.__btn_pendencias_new_file.setCursor(Qt.PointingHandCursor)
        self.__btn_pendencias_new_file.setIcon(QIcon("assets/icon_newfile.png"))
        self.__btn_pendencias_new_file.setObjectName("Buttons_Functions_Directories")
        self.__btn_pendencias_sorting = QPushButton()
        self.__btn_pendencias_sorting.setCursor(Qt.PointingHandCursor)
        self.__btn_pendencias_sorting.setIcon(QIcon("assets/icon_sorting_dark.png"))
        self.__btn_pendencias_sorting.setObjectName("Buttons_Functions_Directories_Sorting")
        self.__btn_pendencias_sorting.setFixedWidth(28)
        layout_btns.addWidget(self.__btn_pendencias_new_folder)
        layout_btns.addWidget(self.__btn_pendencias_new_file)
        layout_btns.addWidget(self.__btn_pendencias_sorting)
        layout_btns.addStretch()

        #...LAYOUT - INFERIOR

        #...LAYOUT - GERAL
        layout.addWidget(container_btns)
        layout.addStretch()

        self.addWidget(self.__pendencias_dir)

    def _setup_pendencias_area(self):
        self.__pendencias_area = QFrame()
        self.__pendencias_area.setObjectName("Frame_Pendencias_Area")
        layout = QVBoxLayout(self.__pendencias_area)

        self.addWidget(self.__pendencias_area)