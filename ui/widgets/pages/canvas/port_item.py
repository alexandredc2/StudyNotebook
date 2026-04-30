from PyQt5.QtCore import Qt, QLineF
from PyQt5.QtGui import QColor, QPen, QBrush
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsLineItem

from ui.widgets.pages.canvas.edge_item import EdgeItem


class PortItem(QGraphicsEllipseItem):
    def __init__(self, x, y, parent=None):
        size = 8
        super().__init__(-size/2, -size/2, size, size, parent)
        self.setPos(x, y)
        self.setPen(QPen(QColor("#ffffff"), 1))
        self.setBrush(QBrush(QColor("#2a2a2a")))
        self.setVisible(False)
        self.setCursor(Qt.CrossCursor)
        self.__temp_line = None
        self.__edges = []

    def add_edge(self, edge):
        self.__edges.append(edge)

    def edges(self):
        return self.__edges

    def mousePressEvent(self, event):
        for item in self.scene().items():
            if isinstance(item, PortItem):
                item.setVisible(True)

        scene_pos = self.scenePos()
        self.__temp_line = QGraphicsLineItem(QLineF(scene_pos, scene_pos))
        self.__temp_line.setPen(QPen(QColor("#ffffff"), 2))
        self.scene().addItem(self.__temp_line)
        event.accept()

    def mouseMoveEvent(self, event):
        if self.__temp_line:
            source = self.scenePos()
            target = event.scenePos()
            self.__temp_line.setLine(QLineF(source, target))
        event.accept()

    def mouseReleaseEvent(self, event):
        self.scene().removeItem(self.__temp_line)
        self.__temp_line = None

        items = self.scene().items(event.scenePos())
        target = next((i for i in items if isinstance(i, PortItem) and i is not self), None)

        for item in self.scene().items():
            if isinstance(item, PortItem):
                item.setVisible(False)

        if target is not None:
            edge = EdgeItem(self, target)
            self.scene().addItem(edge)
            self.add_edge(edge)
            target.add_edge(edge)

        event.accept()