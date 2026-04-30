from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPen
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene

from ui.widgets.pages.canvas.node_item import NodeItem


class BrainstormCanvas(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("BrainstormCanvas")
        self.__scene = QGraphicsScene(self)
        self.__scene.setSceneRect(-5000, -5000, 10000, 10000)
        self.setScene(self.__scene)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def wheelEvent(self, event):
        factor = 1.15 if event.angleDelta().y() > 0 else 1/1.15
        self.scale(factor, factor)

    def mouseDoubleClickEvent(self, event):
        pos = self.mapToScene(event.pos())
        item = self.__scene.itemAt(pos, self.transform())

        if item is None:
            node = NodeItem(pos.x(), pos.y())
            self.__scene.addItem(node)
        else:
            super().mouseDoubleClickEvent(event)