# main.py
import sys
import os

# Setzen Sie QT_IM_MODULE auf 'qtvirtualkeyboard'
os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"

from PySide6.QtCore import Qt 
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QGuiApplication
from src.mainwindow import MainWindow


if __name__ == "__main__":
    # Mainwindow
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())