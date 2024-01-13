# main.py
import sys
import os

# Setzen Sie QT_IM_MODULE auf 'qtvirtualkeyboard'
#os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"

from PySide6.QtGui import QIcon, QFont, QFontDatabase 
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow
from src.ui_MainWindow import Ui_MainWindow
from src.ui_DialogProjectName import Ui_DialogProjectName


 
class DialogProjectName(QMainWindow, Ui_DialogProjectName):
    ''' Klasse die den Dialog zum editieren des Projekt Name erstellt '''    
    def __init__(self, main_window):
        self.main_window = main_window
        super(DialogProjectName, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        
        self.pushButton_Abbrechen.clicked.connect(self.close)
        self.pushButton_OK.clicked.connect(self.okClicked)


        # TODO: 
        # - Positionierung des Dialogfenster arbeitet nicht richtig
        main_x = main_window.pos().x()
        main_y = main_window.pos().y() 
        # Berechne x-Position
        x = main_x + (main_window.width() - self.width()) / 2  
        # Setze y-Position
        y = main_y + 20
        #self.move(x, y)


    def okClicked(self):
        self.changeProjectName()
        self.close()


    def changeProjectName(self):
        self.lineEditProjektName.textChanged.connect(self.main_window.labelProjektname.setText(self.lineEditProjektName.text()))
        '''TODO: 
           Projekname musss zwischengespeichert werden und bei Programmstart wieder geladen werden
           - Dazu muss der Projektname in einer Datei gespeichert werden
        '''
        



class MainWindow(QMainWindow, Ui_MainWindow):
    ''' Klasse die das Hauptfenster erzeugt '''
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint) 
        #self.showFullScreen()

        # dialog fenster projektname
        self.pushButtonProjektname.clicked.connect(self.openDialogProjectName)
        self.dialogProjectName = DialogProjectName(self)
        
        # M2 Resetbutton
        self.m2pushButton.clicked.connect(self.M2ResetClicked)
        
    'Methode zum öffnen des Dialogs zum editieren des Projektnamens '
    def openDialogProjectName(self):
        self.dialogProjectName.show()

    'M2 Resetbutton clicked'    
    def M2ResetClicked(self):
        self.resetM2Lcd()
    
    'setze LCD zurück'
    def resetM2Lcd(self):
        self.m2lcdNumber.display(0)





# Hauptprogramm starten
if __name__ == "__main__":

    # QApplication initialisieren
    app = QApplication(sys.argv)

    # Stylesheet einlesen und anwenden
    with open('./styles.qss', 'r') as f:
        stylesheet = f.read()
    app.setStyleSheet(stylesheet) 

    # Hauptfenster anzeigen    
    main_Window = MainWindow()
    main_Window.show()
    sys.exit(app.exec())

