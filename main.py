# main.py
import sys
import os

from PySide6.QtWidgets import QApplication
from src.MainWindow import MainWindow
from src.config import conf

'Virtuelle Tastatur'
#os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"

'''Stylesheet aus Dateien zusammenführen und anwenden'''
def addStylesheet():
    stylesheet = ''
    theme = conf.value('theme')

    'Stylesheets einlesen' 
    with open('./resources/styles/styles.qss', 'r') as f:
        cssMain = f.read()
    
    with open('./resources/styles/'+theme+'.qss', 'r') as f:
       cssTheme = f.read()
    
    'Beide Stylesheets zusammenführen'
    stylesheet = cssMain + '\n' + cssTheme

    app.setStyleSheet(stylesheet) 



'''Hauptprogramm starten'''
if __name__ == '__main__':

    '''QApplication initialisieren'''
    app = QApplication(sys.argv)
    addStylesheet()

    '''Hauptfenster anzeigen'''   
    main_Window = MainWindow()
    main_Window.show()
    sys.exit(app.exec())

