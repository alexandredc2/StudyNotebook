# -> Bibliotecas importadas:
import os
from PyQt5.QtWidgets import QMainWindow

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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Study Notebook")
        self.setMinimumSize(1200,750)

        # Carrega estilo definido em assets/styles.css
        with open(PATH_STYLES, "r") as f:
            self.setStyleSheet(f.read())
