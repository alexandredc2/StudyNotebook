from PyQt5.QtCore import QRectF, Qt
from PyQt5.QtGui import QPen, QColor, QBrush
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsTextItem

from ui.widgets.pages.canvas.port_item import PortItem
from ui.widgets.pages.canvas.resize_handle import ResizeHandle


class NodeItem(QGraphicsItem):
    def __init__(self, x, y, width=200, height=100):
        super().__init__()
        self.setPos(x, y)
        self.setFlags(
            QGraphicsItem.ItemIsMovable |
            QGraphicsItem.ItemIsSelectable |
            QGraphicsItem.ItemSendsGeometryChanges
        )
        self.__width = width
        self.__height = height
        self.setAcceptHoverEvents(True)
        self.__ports = [
            PortItem(width / 2, 0, self),  # cima
            PortItem(width / 2, height, self),  # baixo
            PortItem(0, height / 2, self),  # esquerda
            PortItem(width, height / 2, self),  # direita
        ]

        self.__handles = [
            ResizeHandle("top_left", self),
            ResizeHandle("top_right", self),
            ResizeHandle("bottom_left", self),
            ResizeHandle("bottom_right", self),
        ]
        self._update_handles()

        self.__text = QGraphicsTextItem(self)
        self.__text.setDefaultTextColor(QColor("#ffffff"))
        self.__text.setPos(10, 10)
        self.__text.setTextWidth(self.__width - 20)

    def resize(self, position, delta, start_rect, start_node_pos):
        min_size = 40

        new_width = start_rect.width()
        new_height = start_rect.height()
        new_x = start_node_pos.x()
        new_y = start_node_pos.y()

        if position == "bottom_right":
            new_width = max(min_size, start_rect.width() + delta.x())
            new_height = max(min_size, start_rect.height() + delta.y())
        elif position == "bottom_left":
            new_width = max(min_size, start_rect.width() - delta.x())
            new_height = max(min_size, start_rect.height() + delta.y())
            new_x = start_node_pos.x() + (start_rect.width() - new_width)
        elif position == "top_right":
            new_width = max(min_size, start_rect.width() + delta.x())
            new_height = max(min_size, start_rect.height() - delta.y())
            new_y = start_node_pos.y() + (start_rect.height() - new_height)
        elif position == "top_left":
            new_width = max(min_size, start_rect.width() - delta.x())
            new_height = max(min_size, start_rect.height() - delta.y())
            new_x = start_node_pos.x() + (start_rect.width() - new_width)
            new_y = start_node_pos.y() + (start_rect.height() - new_height)

        self.__width = new_width
        self.__height = new_height
        self.prepareGeometryChange()
        self.setPos(new_x, new_y)
        self.__text.setTextWidth(self.__width - 20)
        self._update_handles()
        self._update_ports()

    def _update_ports(self):
        positions = [
            (self.__width / 2, 0),
            (self.__width / 2, self.__height),
            (0, self.__height / 2),
            (self.__width, self.__height / 2),
        ]
        for port, (x, y) in zip(self.__ports, positions):
            port.setPos(x, y)
            for edge in port.edges():
                edge.update_position()

    def _update_handles(self):
        positions = {
            "top_left": (0, 0),
            "top_right": (self.__width, 0),
            "bottom_left": (0, self.__height),
            "bottom_right": (self.__width, self.__height),
        }
        for handle in self.__handles:
            x, y = positions[handle.position()]
            handle.setPos(x, y)

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionHasChanged:
            for port in self.__ports:
                for edge in port.edges():
                    edge.update_position()
        if change == QGraphicsItem.ItemSelectedHasChanged:
            for handle in self.__handles:
                handle.setVisible(bool(value))
        return super().itemChange(change, value)

    def boundingRect(self):
        return QRectF(0, 0, self.__width, self.__height)

    def paint(self, painter, option, widget):
        painter.drawRect(self.boundingRect())
        painter.setPen(QPen(QColor("#ffffff"), 2))
        #painter.setBrush(QBrush(QColor("#2a2a2a")))
        painter.drawRect(self.boundingRect())

    def hoverEnterEvent(self, event):
        for port in self.__ports:
            port.setVisible(True)

    def hoverLeaveEvent(self, event):
        for port in self.__ports:
            port.setVisible(False)

    def mouseDoubleClickEvent(self, event):
        self.__text.setTextInteractionFlags(Qt.TextEditorInteraction)
        self.__text.setFocus()
        event.accept()
