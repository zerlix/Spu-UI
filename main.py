# main.py
import sys
import os

'Virtuelle Tastatur'
#os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"

from PySide6.QtWidgets import QApplication
from src.MainWindow import MainWindow

"TODO: Muss aus Configuration geladen werden"
theme = './resources/styles/light.qss'
#theme = './resources/styles/dark.qss'



"""Stylesheet aus Dateien zusammenführen"""
def add_stylesheets():
    stylesheet = ''
    
    "Stylesheets einlesen" 
    with open('./resources/styles/styles.qss', 'r') as f:
        cssMain = f.read()
    
    with open(theme, 'r') as f:
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

