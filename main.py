# main.py
import sys
import os

from PySide6.QtCore import QSettings, QStandardPaths
from PySide6.QtWidgets import QApplication
from src.MainWindow import MainWindow

''' Konfigurationsdatei laden '''
cfg_file = QSettings('./config.ini', QSettings.IniFormat)


'Virtuelle Tastatur'
#os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"

"""Stylesheet aus Dateien zusammenführen"""
def add_stylesheets():
    stylesheet = ''
    
    "Stylesheets einlesen" 
    with open('./resources/styles/styles.qss', 'r') as f:
        cssMain = f.read()
    
    theme = cfg_file.value('theme')
    
    print("Theme: "+theme)

    with open("./resources/styles/"+theme+".qss", 'r') as f:
       cssTheme = f.read()
    
    "Beide Stylesheets zusammenführen"
    stylesheet = cssMain + "\n" + cssTheme

    app.setStyleSheet(stylesheet) 



"""Hauptprogramm starten"""
if __name__ == "__main__":

    """QApplication initialisieren"""
    app = QApplication(sys.argv)
    add_stylesheets();

    """Hauptfenster anzeigen"""   
    main_Window = MainWindow()
    main_Window.show()
    sys.exit(app.exec())

