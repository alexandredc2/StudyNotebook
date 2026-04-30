from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QButtonGroup
from assets.style import directories_style


class Directories(QFrame):
    view_changed = pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Frame_Directories")
        self.setStyleSheet(directories_style())

        #Configuração do Layout deste objeto:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20,20,20,0)
        layout.setSpacing(5)

        self.__finder_area = QFrame()
        self.__finder_area.setFixedHeight(30)
        self.__finder_area.setObjectName("Frame_Directories_Finder_Area")

        self.__folders_area = QFrame()
        self.__folders_area.setObjectName("Frame_Directories_Folders_Area")

        layout.addWidget(self.__finder_area)
        layout.addWidget(self.__folders_area)

        self._setup_finder_area()
        self._setup_folders_area()

    def _setup_finder_area(self):
        layout = QHBoxLayout(self.__finder_area)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(10)

        self.__finder_area_icon = QLabel()
        pixmap = QPixmap("assets/icon_finder_area.png")
        pixmap = pixmap.scaled(16, 16, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.__finder_area_icon.setPixmap(pixmap)

        self.__finder_area_input = QLineEdit()
        self.__finder_area_input.setObjectName("Finder_Area_Input")
        self.__finder_area_input.setPlaceholderText("Procurar...")

        layout.addWidget(self.__finder_area_icon)
        layout.addWidget(self.__finder_area_input)

    def _setup_folders_area(self):
        layout = QVBoxLayout(self.__folders_area)
        layout.setContentsMargins(0,10,0,0)
        layout.setSpacing(5)

        self.__btn_home = QPushButton("  Tela de Início")
        self.__btn_home.setIcon(QIcon("assets/icon_home_dark.png"))
        self.__btn_home.setFixedWidth(198)
        self.__btn_home.setCheckable(True)
        self.__btn_home.setCursor(Qt.PointingHandCursor)
        self.__btn_home.setObjectName("Folders_Area_Buttons")

        self.__btn_notebooks = QPushButton("  Cadernos")
        self.__btn_notebooks.setIcon(QIcon("assets/icon_notebook_dark.png"))
        self.__btn_notebooks.setFixedWidth(198)
        self.__btn_notebooks.setCheckable(True)
        self.__btn_notebooks.setCursor(Qt.PointingHandCursor)
        self.__btn_notebooks.setObjectName("Folders_Area_Buttons")

        self.__btn_tasks = QPushButton("  Pendências")
        self.__btn_tasks.setIcon(QIcon("assets/icon_tasks_dark.png"))
        self.__btn_tasks.setFixedWidth(198)
        self.__btn_tasks.setCheckable(True)
        self.__btn_tasks.setCursor(Qt.PointingHandCursor)
        self.__btn_tasks.setObjectName("Folders_Area_Buttons")

        self.__btn_brainstorm = QPushButton("  Mapas Mentais")
        self.__btn_brainstorm.setIcon(QIcon("assets/icon_brainstorm_dark.png"))
        self.__btn_brainstorm.setFixedWidth(198)
        self.__btn_brainstorm.setCheckable(True)
        self.__btn_brainstorm.setCursor(Qt.PointingHandCursor)
        self.__btn_brainstorm.setObjectName("Folders_Area_Buttons")

        self.__btn_languages = QPushButton("  Revisão Idiomas")
        self.__btn_languages.setIcon(QIcon("assets/icon_languages_dark.png"))
        self.__btn_languages.setFixedWidth(198)
        self.__btn_languages.setCheckable(True)
        self.__btn_languages.setCursor(Qt.PointingHandCursor)
        self.__btn_languages.setObjectName("Folders_Area_Buttons")

        self.__grupo_de_btns = QButtonGroup()
        self.__grupo_de_btns.addButton(self.__btn_home)
        self.__grupo_de_btns.addButton(self.__btn_notebooks)
        self.__grupo_de_btns.addButton(self.__btn_tasks)
        self.__grupo_de_btns.addButton(self.__btn_brainstorm)
        self.__grupo_de_btns.addButton(self.__btn_languages)

        layout.addWidget(self.__btn_home)
        layout.addWidget(self.__btn_notebooks)
        layout.addWidget(self.__btn_tasks)
        layout.addWidget(self.__btn_brainstorm)
        layout.addWidget(self.__btn_languages)
        layout.addStretch()

        self.__btn_home.clicked.connect(lambda: self.view_changed.emit(0))
        self.__btn_notebooks.clicked.connect(lambda: self.view_changed.emit(1))
        self.__btn_tasks.clicked.connect(lambda: self.view_changed.emit(2))
        self.__btn_brainstorm.clicked.connect(lambda: self.view_changed.emit(3))
        self.__btn_languages.clicked.connect(lambda: self.view_changed.emit(4))


