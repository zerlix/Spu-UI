# main.py
import sys
import os

'Virtuelle Tastatur'
#os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow
from src.ui_MainWindow import Ui_MainWindow
from src.DialogProjectName import DialogProjectName


class MainWindow(QMainWindow, Ui_MainWindow):
    ''' Klasse die das Hauptfenster erzeugt '''
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint) 
        'self.showFullScreen()'

        'dialog fenster projektname'
        self.pushButtonProjektname.clicked.connect(self.openDialogProjectName)
        self.dialogProjectName = DialogProjectName(self)
        
        'm² Resetbutton'
        self.m2pushButton.clicked.connect(self.M2ResetClicked)
        

    'Methode zum öffnen des Dialogs zum editieren des Projektnamens '
    def openDialogProjectName(self):
        self.dialogProjectName.show()


    'm² Resetbutton clicked'    
    def M2ResetClicked(self):
        self.resetM2Lcd()


    'setze m² LCD zurück'
    def resetM2Lcd(self):
        self.m2lcdNumber.display(0)


'Hauptprogramm starten'
if __name__ == "__main__":

    'QApplication initialisieren'
    app = QApplication(sys.argv)

    'Stylesheet einlesen und anwenden'
    with open('./styles.qss', 'r') as f:
        stylesheet = f.read()
    app.setStyleSheet(stylesheet) 

    'Hauptfenster anzeigen'    
    main_Window = MainWindow()
    main_Window.show()
    sys.exit(app.exec())

