from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QColor, QBrush
from PyQt5.QtWidgets import QGraphicsRectItem


class ResizeHandle(QGraphicsRectItem):
    def __init__(self, position, parent=None):
        size = 8
        super().__init__(-size/2, -size/2, size, size, parent)
        self.setPen(QPen(QColor("#ffffff"), 1))
        self.setBrush(QBrush(QColor("#ffffff")))
        self.setCursor(Qt.SizeFDiagCursor)
        self.setVisible(False)
        self.__position = position  # "top_left", "top_right", "bottom_left", "bottom_right"
        self.__start_pos = None
        self.__start_rect = None

    def position(self):
        return self.__position

    def mousePressEvent(self, event):
        self.__start_pos = event.scenePos()
        self.__start_rect = self.parentItem().boundingRect()
        self.__start_node_pos = self.parentItem().pos()  # <- adiciona isso
        event.accept()

    def mouseMoveEvent(self, event):
        delta = event.scenePos() - self.__start_pos
        self.parentItem().resize(self.__position, delta, self.__start_rect, self.__start_node_pos)
        event.accept()

    def mouseReleaseEvent(self, event):
        event.accept()