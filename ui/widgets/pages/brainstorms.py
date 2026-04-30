import uuid

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFrame, QSplitter, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QTreeWidget, \
    QTreeWidgetItem, QTabWidget

from ui.widgets.pages.canvas.brainstorm_canvas import BrainstormCanvas


class Brainstorms(QSplitter):
    def __init__(self, parent=None):
        super().__init__(Qt.Horizontal, parent)
        self.setObjectName("Splitter_Functions")

        self._setup_brainstorms_directories()
        self._setup_brainstorms_area()
        self.setSizes([295, 800])

    def _setup_brainstorms_directories(self):
        self.__brainstorms_dir = QFrame()
        self.__brainstorms_dir.setContentsMargins(10,2,10,20)
        self.__brainstorms_dir.setObjectName("Frame_Buttons_Directories")
        self.__brainstorms_dir.setMinimumWidth(295)
        self.__brainstorms_dir.setMaximumWidth(350)
        layout = QVBoxLayout(self.__brainstorms_dir)

        #...LAYOUT - SUPERIOR
        container_btns = QFrame()
        layout_btns = QHBoxLayout(container_btns)
        self.__btn_brainstorms_new_folder = QPushButton("  Nova Pasta")
        self.__btn_brainstorms_new_folder.setCursor(Qt.PointingHandCursor)
        self.__btn_brainstorms_new_folder.setIcon(QIcon("assets/icon_newfolder.png"))
        self.__btn_brainstorms_new_folder.setObjectName("Buttons_Functions_Directories")
        self.__btn_brainstorms_new_file = QPushButton("  Novo Arquivo")
        self.__btn_brainstorms_new_file.setCursor(Qt.PointingHandCursor)
        self.__btn_brainstorms_new_file.setIcon(QIcon("assets/icon_newfile.png"))
        self.__btn_brainstorms_new_file.setObjectName("Buttons_Functions_Directories")
        self.__btn_sorting = QPushButton()
        self.__btn_sorting.setCursor(Qt.PointingHandCursor)
        self.__btn_sorting.setIcon(QIcon("assets/icon_sorting_dark.png"))
        self.__btn_sorting.setObjectName("Buttons_Functions_Directories_Sorting")
        self.__btn_sorting.setFixedWidth(28)
        layout_btns.addWidget(self.__btn_brainstorms_new_folder)
        layout_btns.addWidget(self.__btn_brainstorms_new_file)
        layout_btns.addWidget(self.__btn_sorting)
        layout_btns.addStretch()

        #...LAYOUT - INFERIOR
        label = QLabel("DIRETÓRIOS")
        label.setObjectName("Label_Directories_General")

        self.__brainstorms_tree = QTreeWidget()
        self.__brainstorms_tree.setHeaderHidden(True)
        self.__brainstorms_tree.setObjectName("Trees_Functions_Directories")
        self.__brainstorms_tree.setDragEnabled(True)
        self.__brainstorms_tree.setAcceptDrops(True)
        self.__brainstorms_tree.setDropIndicatorShown(True)
        self.__brainstorms_tree.setDragDropMode(QTreeWidget.InternalMove)

        #...LAYOUT - GERAL
        layout.addWidget(container_btns)
        layout.addWidget(label)
        layout.addWidget(self.__brainstorms_tree)
        #layout.addStretch()

        self.addWidget(self.__brainstorms_dir)

        #...AÇÕES DE BOTÕES
        self.__btn_brainstorms_new_folder.clicked.connect(self._function_add_folder)
        self.__btn_brainstorms_new_file.clicked.connect(self._function_add_file)
        self.__brainstorms_tree.itemDoubleClicked.connect(self._open_brainstorm)

    def _function_add_folder(self):
        folder = QTreeWidgetItem(self.__brainstorms_tree)
        folder.setText(0,"Nova Pasta")
        folder.setIcon(0, QIcon("assets/icon_folder_dark.png"))
        folder.setFlags(folder.flags() | Qt.ItemIsEditable)
        folder.setData(0, Qt.UserRole, "folder")
        folder.setData(0, Qt.UserRole + 1, str(uuid.uuid4()))
        self.__brainstorms_tree.addTopLevelItem(folder)
        self.__brainstorms_tree.editItem(folder, 0)

    def _function_add_file(self):
        selected = self.__brainstorms_tree.currentItem()

        file = QTreeWidgetItem()
        file.setText(0,"Novo Arquivo")
        file.setIcon(0, QIcon("assets/icon_brainmap_dark.png"))
        file.setFlags(file.flags() | Qt.ItemIsEditable)
        file.setData(0, Qt.UserRole, "file")
        file.setData(0, Qt.UserRole + 1, str(uuid.uuid4()))

        if selected is not None:
            selected.addChild(file)
            selected.setExpanded(True)
        else:
            self.__brainstorms_tree.addTopLevelItem(file)
        self.__brainstorms_tree.editItem(file, 0)

    def _setup_brainstorms_area(self):
        self.__brainstorms_area = QTabWidget()
        self.__brainstorms_area.tabBar().setCursor(Qt.PointingHandCursor)
        self.__brainstorms_area.setObjectName("Tabs_Brainstorms_Area")
        self.__brainstorms_area.setTabsClosable(True)
        self.__brainstorms_area.tabCloseRequested.connect(self.__brainstorms_area.removeTab)
        self.addWidget(self.__brainstorms_area)

    def _open_brainstorm(self, item):
        if item.data(0, Qt.UserRole) != "file":
            return

        file_id = item.data(0, Qt.UserRole + 1)

        # Verifica se a aba já está aberta:
        for i in range(self.__brainstorms_area.count()):
            widget = self.__brainstorms_area.widget(i)
            if widget.property("file_id") == file_id:
                self.__brainstorms_area.setCurrentIndex(i)
                return

        canvas = BrainstormCanvas()
        canvas.setProperty("file_id", file_id)
        self.__brainstorms_area.addTab(canvas, item.text(0))
        self.__brainstorms_area.setCurrentWidget(canvas)