# main.py
import sys
import os

'Virtuelle Tastatur'
#os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"

from PySide6.QtWidgets import QApplication
from src.MainWindow import MainWindow



"""Hauptprogramm starten"""
if __name__ == "__main__":

    """QApplication initialisieren"""
    app = QApplication(sys.argv)

    """Stylesheet einlesen und anwenden"""
    with open('./styles.qss', 'r') as f:
        stylesheet = f.read()
    app.setStyleSheet(stylesheet) 

    """Hauptfenster anzeigen"""   
    main_Window = MainWindow()
    main_Window.show()
    sys.exit(app.exec())

