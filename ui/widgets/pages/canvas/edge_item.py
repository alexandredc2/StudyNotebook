from PyQt5.QtCore import QLineF
from PyQt5.QtGui import QColor, QPen
from PyQt5.QtWidgets import QGraphicsLineItem


class EdgeItem(QGraphicsLineItem):
    def __init__(self, source_port, target_port):
        super().__init__()
        self.__source = source_port
        self.__target = target_port
        self.setPen(QPen(QColor("#ffffff"), 0.5))
        self.update_position()

    def update_position(self):
        source_pos = self.__source.scenePos()
        target_pos = self.__target.scenePos()
        self.setLine(QLineF(source_pos, target_pos))