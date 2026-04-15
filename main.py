# -> Bibliotecas importadas:
import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow
from database.connection import DatabaseManager

if __name__ == '__main__':
    banco = DatabaseManager()
    app = QApplication(sys.argv)
    window = MainWindow(banco)
    window.show()
    sys.exit(app.exec_())