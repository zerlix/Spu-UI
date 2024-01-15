# main.py
import sys
import os

from PySide6.QtWidgets import QApplication
from src.MainWindow import MainWindow
from src.config import *

'Virtuelle Tastatur'
#os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"



'''Hauptprogramm starten'''
if __name__ == '__main__':

    '''QApplication initialisieren'''
    app = QApplication(sys.argv)
    app.setStyleSheet(merge_Stylesheet()) 
    #addStylesheet()

    '''Hauptfenster anzeigen'''   
    main_Window = MainWindow()
    main_Window.show()
    sys.exit(app.exec())

