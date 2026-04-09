# -> Bibliotecas importadas:
import os
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QSplitter, QWidget, QVBoxLayout, QTreeWidget, QMenu, QTreeWidgetItem, \
    QScrollArea

# -> Constantes e arquivos importados:
PATH_ICON_CENTER_ALIGN = os.path.join(os.path.dirname(__file__), "..", "assets", "icon_center_align.png")
PATH_ICON_FONT = os.path.join(os.path.dirname(__file__), "..", "assets", "icon_font.png")
PATH_ICON_FONT_DOWN = os.path.join(os.path.dirname(__file__), "..", "assets", "icon_font_down.png")
PATH_ICON_FONT_UP = os.path.join(os.path.dirname(__file__), "..", "assets", "icon_font_up.png")
PATH_ICON_JUSTIFY_ALIGN = os.path.join(os.path.dirname(__file__), "..", "assets", "icon_justify_align.png")
PATH_ICON_LEFT_ALIGN = os.path.join(os.path.dirname(__file__), "..", "assets", "icon_left_align.png")
PATH_ICON_LIST = os.path.join(os.path.dirname(__file__), "..", "assets", "icon_list.png")
PATH_ICON_RIGHT_ALIGN = os.path.join(os.path.dirname(__file__), "..", "assets", "icon_right_align.png")
PATH_STYLES = os.path.join(os.path.dirname(__file__), "..", "assets", "styles.css")
PATH_ICON_FOLDER_CLOSED = os.path.join(os.path.dirname(__file__), "..", "assets", "icon_folder_closed.png")
PATH_ICON_FOLDER_OPEN = os.path.join(os.path.dirname(__file__), "..", "assets", "icon_folder_open.png")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Study Notebook")
        self.setMinimumSize(1200,750)

        # Carrega estilo definido em assets/styles.css
        with open(PATH_STYLES, "r") as f:
            self.setStyleSheet(f.read())

        self._setup_ui()

    def _setup_ui(self):
        # Definição de Layouts existentes:
        self.layout_mainwindow = QSplitter(Qt.Horizontal)
        self.layout_pastas = QVBoxLayout()
        self.layout_documento = QVBoxLayout()
        self.setCentralWidget(self.layout_mainwindow)

        # Definição de Widgets:
        self.painel_pastas = QWidget()
        self.painel_pastas.setObjectName("setup_ui_pastas")
        self.painel_documento = QWidget()
        self.painel_documento.setObjectName("setup_ui_documento")
        self.layout_mainwindow.addWidget(self.painel_pastas)
        self.layout_mainwindow.addWidget(self.painel_documento)
        self.layout_mainwindow.setSizes([220, 980])

        # Cria o Menu Superior:
        menu_bar = self.menuBar()
        menu_file = menu_bar.addMenu("Arquivo")
        menu_tools = menu_bar.addMenu("Ferramentas")
        menu_help = menu_bar.addMenu("Ajuda")
        menu_about = menu_bar.addMenu("Sobre")

        # Cria o Rodapé:
        status_bar = self.statusBar()

        # Chama a função de estilização do painel de pastas:
        self._setup_ui_pastas()

        # Chama a função de estilização do painel de documento:
        self._setup_ui_documento()

    def _setup_ui_pastas(self):
        # Define o layout do widget
        self.painel_pastas.setLayout(self.layout_pastas)

        # Objetos que serão utilizados dentro do layout
        self.arvore_pastas = QTreeWidget()
        self.arvore_pastas.setObjectName("setup_ui_arvore_pastas")
        self.arvore_pastas.setHeaderHidden(True)
        self.arvore_pastas.setContextMenuPolicy(Qt.CustomContextMenu)
        self.arvore_pastas.customContextMenuRequested.connect(self._setup_ui_pastas_menu)

        # Inserção de Objetos no layout:
        self.layout_pastas.addWidget(self.arvore_pastas)

    def _setup_ui_pastas_menu(self, position):
        item = self.arvore_pastas.itemAt(position)

        menu = QMenu()

        act_criar_pasta = menu.addAction("Nova Pasta")
        act_renomear_pasta = menu.addAction("Renomear Pasta")
        act_deletar_pasta = menu.addAction("Deletar Pasta")

        action = menu.exec_(self.arvore_pastas.viewport().mapToGlobal(position))

        if action == act_criar_pasta:
            self._setup_ui_pastas_criar()
        elif action == act_renomear_pasta:
            pass
        elif action == act_deletar_pasta:
            pass

    def _setup_ui_pastas_criar(self, nome="Nova Pasta"):
        item = QTreeWidgetItem(self.arvore_pastas,[nome])
        item.setIcon(0,QIcon(PATH_ICON_FOLDER_CLOSED))
        return item

    def _setup_ui_documento(self):
        # Define o layout do widget
        self.painel_documento.setLayout(self.layout_documento)

        # Objetos que serão utilizados dentro do layout
        self.documento_formatacao = QWidget()
        self.documento_formatacao.setObjectName("setup_ui_documento_formatacao")
        self.documento_formatacao.setMinimumHeight(60)
        self.documento_area = QScrollArea()
        self.documento_area.setObjectName("setup_ui_documento_area")

        # Inserção de Objetos no layout:
        self.layout_documento.addWidget(self.documento_formatacao)
        self.layout_documento.addWidget(self.documento_area)


