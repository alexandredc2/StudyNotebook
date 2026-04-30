from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMenuBar, QFrame, QHBoxLayout, QPushButton

from assets.style import menubar_style


class MenuBar(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("MenuBar")
        self.setStyleSheet(menubar_style())

        self._setup_window_functions()

        #Variáveis
        self._drag_pos = None

    def _setup_window_functions(self):
        container = QFrame()
        container.setObjectName("Frame_MenuBar_Functions")
        layout = QHBoxLayout(container)

        self.__btn_view_mode = QPushButton()
        self.__btn_fullscreen = QPushButton()
        self.__btn_quit_window = QPushButton()
        self.__btn_view_mode.setIcon(QIcon("assets/icon_viewmode_dark.png"))
        self.__btn_fullscreen.setIcon(QIcon("assets/icon_full_dark.png"))
        self.__btn_quit_window.setIcon(QIcon("assets/icon_quit_dark.png"))
        self.__btn_view_mode.setObjectName("Frame_MenuBar_Functions_Buttons")
        self.__btn_fullscreen.setObjectName("Frame_MenuBar_Functions_Buttons")
        self.__btn_quit_window.setObjectName("Frame_MenuBar_Functions_Buttons")
        self.__btn_view_mode.setCursor(Qt.PointingHandCursor)
        self.__btn_fullscreen.setCursor(Qt.PointingHandCursor)
        self.__btn_quit_window.setCursor(Qt.PointingHandCursor)

        layout.addWidget(self.__btn_view_mode)
        layout.addWidget(self.__btn_fullscreen)
        layout.addWidget(self.__btn_quit_window)

        self.setCornerWidget(container, Qt.TopRightCorner)

        self.__btn_quit_window.clicked.connect(lambda: self.window().close())

    #Funções de sobreescrita de eventos de mouse:
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._drag_pos = event.globalPos() - self.window().frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self._drag_pos is not None:
            self.window().move(event.globalPos() - self._drag_pos)
            event.accept()

    def mouseReleaseEvent(self, event):
        self._drag_pos = None
        event.accept()

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.window().isMaximized():
                self.window().showNormal()
            else:
                self.window().showMaximized()
            event.accept()
