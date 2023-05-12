import sys
# import os
# import time
# import math
# import pyqtgraph as pg
from PyQt6.QtWidgets import QApplication, QMainWindow
#from PyQt6.QtWidgets import QPushButton, QFileDialog, QComboBox, QLineEdit, QLabel
# from PyQt6.QtGui import QIcon
# from PyQt6.QtCore import QTimer

from ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.initUI()

    def initUI(self):
        #self.statusBar().showMessage('When you : bottom text')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec())  # replace exec_() with exec()
