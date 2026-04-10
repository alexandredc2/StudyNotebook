# -> Bibliotecas importadas:
import os
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QMainWindow, QSplitter, QWidget, QVBoxLayout, QHBoxLayout, QTreeWidget, QMenu, \
    QTreeWidgetItem, \
    QScrollArea, QComboBox, QPushButton, QFrame, QTextEdit

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
PATH_ICON_FONT_BOLD = os.path.join(os.path.dirname(__file__), "..", "assets", "icon_negrito.png")
PATH_ICON_FONT_ITALIC = os.path.join(os.path.dirname(__file__), "..", "assets", "icon_italic.png")
PATH_ICON_FONT_UNDERLINE = os.path.join(os.path.dirname(__file__), "..", "assets", "icon_underline.png")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Study Notebook")
        self.setMinimumSize(1200,750)

        # Carrega estilo definido em assets/styles.css
        with open(PATH_STYLES, "r") as f:
            self.setStyleSheet(f.read())

        # Variáveis auxiliares para funções implementadas:
        self.zoom_fator = 1.0

        self._setup_ui()
        self._setup_ui_pastas()
        self._setup_ui_documento()
        self._setup_ui_documento_formatacao()
        self._setup_ui_documento_folha()
        self._connect_signals()

    def _connect_signals(self):
        # Conexão de funções referentes a aba de formatação de textos
        self.selec_tamanho_texto.currentTextChanged.connect(self._setup_caderno_tamanho_texto)
        self.selec_font_negrito.clicked.connect(self._setup_caderno_toggle_negrito)
        self.selec_font_italico.clicked.connect(self._setup_caderno_toggle_italico)
        self.selec_font_sublinhado.clicked.connect(self._setup_caderno_toggle_sublinhado)
        self.caderno.cursorPositionChanged.connect(self._setup_caderno_atualizar_toolbar)
        self.selec_texto_ident_left.clicked.connect(lambda: self._setup_caderno_ident(Qt.AlignLeft))
        self.selec_texto_ident_center.clicked.connect(lambda: self._setup_caderno_ident(Qt.AlignCenter))
        self.selec_texto_ident_right.clicked.connect(lambda: self._setup_caderno_ident(Qt.AlignRight))
        self.selec_texto_ident_justify.clicked.connect(lambda: self._setup_caderno_ident(Qt.AlignJustify))

        # Conexão referente a função de zoom in e zoom out da página de cadernos
        self.documento_area.installEventFilter(self)
        self.documento_area.viewport().installEventFilter(self)

    def eventFilter(self,obj,event):
        # Essa função é responsável pelo controle de zoom in e zoom out do documento de texto
        if obj in (self.documento_area, self.documento_area.viewport()) and event.type() == QEvent.Wheel:
            if event.modifiers() == Qt.ControlModifier:
                delta = event.angleDelta().y()
                if delta > 0:
                    self.zoom_fator = min(3.0, self.zoom_fator+0.1)
                    self.caderno.zoomIn(1)
                else:
                    self.zoom_fator = max(0.3, self.zoom_fator-0.1)
                    self.caderno.zoomOut(1)
                self._aplicar_zoom_documento()
                return True # consome o evento, não scrolla
        return super().eventFilter(obj,event)

    def _aplicar_zoom_documento(self):
        base_w = 794
        base_h = 1123
        nova_w = int(base_w * self.zoom_fator)
        nova_h = int(base_h * self.zoom_fator)
        self.documento_folha.setFixedSize(nova_w, nova_h)

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
        self.documento_canvas = QWidget()
        self.documento_canvas.setObjectName("setup_ui_documento_canvas")
        layout_canvas = QVBoxLayout(self.documento_canvas)
        layout_canvas.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        layout_canvas.setContentsMargins(0,40,0,40)
        self.documento_folha = QWidget()
        self.documento_folha.setObjectName("setup_ui_documento_folha")
        self.documento_folha.setFixedSize(794,1123)
        self.documento_area.setWidgetResizable(True)
        self.documento_area.setWidget(self.documento_canvas)

        # Inserção de Objetos no layout:
        self.layout_documento.addWidget(self.documento_formatacao)
        self.layout_documento.addWidget(self.documento_area)
        layout_canvas.addWidget(self.documento_folha)

    def _setup_ui_documento_formatacao(self):
        layout_formatacao = QHBoxLayout(self.documento_formatacao)

        # Objetos que serão utilizados:
        self.selec_tipo_texto = QComboBox()
        self.selec_tipo_texto.addItems(['Normal','Título 1','Título 2','Título 3'])
        self.selec_tamanho_texto = QComboBox()
        self.selec_tamanho_texto.addItems(['6','7','8','9','10','11','12','13','14','16','18','20','24','28'])
        self.selec_tamanho_texto.setCurrentText('8')
        self.selec_font_negrito = QPushButton()
        self.selec_font_negrito.setCheckable(True)
        self.selec_font_italico = QPushButton()
        self.selec_font_italico.setCheckable(True)
        self.selec_font_sublinhado = QPushButton()
        self.selec_font_sublinhado.setCheckable(True)
        self.selec_font_negrito.setIcon(QIcon(PATH_ICON_FONT_BOLD))
        self.selec_font_italico.setIcon(QIcon(PATH_ICON_FONT_ITALIC))
        self.selec_font_sublinhado.setIcon(QIcon(PATH_ICON_FONT_UNDERLINE))
        self.selec_texto_ident_left = QPushButton()
        self.selec_texto_ident_right = QPushButton()
        self.selec_texto_ident_center = QPushButton()
        self.selec_texto_ident_justify = QPushButton()
        separador = QFrame()
        separador.setFrameShape(QFrame.VLine)
        self.selec_texto_ident_left.setIcon(QIcon(PATH_ICON_LEFT_ALIGN))
        self.selec_texto_ident_right.setIcon(QIcon(PATH_ICON_RIGHT_ALIGN))
        self.selec_texto_ident_center.setIcon(QIcon(PATH_ICON_CENTER_ALIGN))
        self.selec_texto_ident_justify.setIcon(QIcon(PATH_ICON_JUSTIFY_ALIGN))
        layout_formatacao.addWidget(self.selec_tipo_texto)
        layout_formatacao.addWidget(self.selec_tamanho_texto)
        layout_formatacao.addWidget(self.selec_font_negrito)
        layout_formatacao.addWidget(self.selec_font_italico)
        layout_formatacao.addWidget(self.selec_font_sublinhado)
        layout_formatacao.addWidget(separador)
        layout_formatacao.addWidget(self.selec_texto_ident_left)
        layout_formatacao.addWidget(self.selec_texto_ident_right)
        layout_formatacao.addWidget(self.selec_texto_ident_center)
        layout_formatacao.addWidget(self.selec_texto_ident_justify)
        layout_formatacao.addStretch()

    def _setup_ui_documento_folha(self):
        # Definição de layout
        layout_folha = QVBoxLayout(self.documento_folha)
        layout_folha.setContentsMargins(40,40,40,40)

        # Objetos que serão utilizados
        self.caderno = QTextEdit()
        self.caderno.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.caderno.setObjectName("setup_ui_caderno")

        # Inserção dos objetos no layout
        layout_folha.addWidget(self.caderno)

    def _setup_caderno_tamanho_texto(self,tamanho):
        fmt = self.caderno.currentCharFormat()
        fmt.setFontPointSize(float(tamanho))
        self.caderno.mergeCurrentCharFormat(fmt)

    def _setup_caderno_toggle_negrito(self):
        # Primariamente, essa função tem como objeto ativar e desabilitar a função negrito aos textos.
        fmt = self.caderno.currentCharFormat()
        is_bold = self.selec_font_negrito.isChecked()
        fmt.setFontWeight(QFont.Bold if is_bold else QFont.Normal)
        self.caderno.mergeCurrentCharFormat(fmt)

    def _setup_caderno_toggle_italico(self):
        # Primariamente, essa função tem como objeto ativar e desabilitar a função itálico aos textos.
        fmt = self.caderno.currentCharFormat()
        is_italic = self.selec_font_italico.isChecked()
        fmt.setFontItalic(is_italic)
        self.caderno.mergeCurrentCharFormat(fmt)

    def _setup_caderno_toggle_sublinhado(self):
        # Primariamente, essa função tem como objeto ativar e desabilitar a função sublinhado aos textos.
        fmt = self.caderno.currentCharFormat()
        is_sublinhado = self.selec_font_sublinhado.isChecked()
        fmt.setFontUnderline(is_sublinhado)
        self.caderno.mergeCurrentCharFormat(fmt)

    def _setup_caderno_ident(self,alinhamento):
        self.caderno.setAlignment(alinhamento)

    def _setup_caderno_atualizar_toolbar(self):
        # Primariamente, essa função tem como objetivo verificar textos que já tem o negrito, italico
        # ou sublinhado ativo para que atualize a toolbar corretamente.
        fmt = self.caderno.currentCharFormat()
        self.selec_font_negrito.setChecked(fmt.fontWeight() == QFont.Bold)
        self.selec_font_italico.setChecked(fmt.fontItalic())
        self.selec_font_sublinhado.setChecked(fmt.fontUnderline())

        # O trecho abaixo é para atualizar o tamanho da fonte quando diferentes textos forem selecionados
        tamanho = int(fmt.fontPointSize())
        if tamanho <= 0:
            tamanho = 8
        self.selec_tamanho_texto.blockSignals(True)
        self.selec_tamanho_texto.setCurrentText(str(tamanho))
        self.selec_tamanho_texto.blockSignals(False)
