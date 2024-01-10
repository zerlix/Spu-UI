# main.py
import sys
import os

# Setzen Sie QT_IM_MODULE auf 'qtvirtualkeyboard'
os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"

from PySide6.QtCore import Qt 
from PySide6.QtWidgets import QApplication, QMainWindow
from src.MainWindow_ui import Ui_MainWindow
        


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)




if __name__ == "__main__":
    # Mainwindow
    app = QApplication(sys.argv)

    main_Window = MainWindow()
    main_Window.show()
    

    sys.exit(app.exec())