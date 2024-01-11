# main.py
import sys
import os

# Setzen Sie QT_IM_MODULE auf 'qtvirtualkeyboard'
#os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"

from PySide6.QtGui import QIcon 
from PySide6.QtWidgets import QApplication, QMainWindow
from src.ui_MainWindow import Ui_MainWindow
from src.ui_DialogProjectName import Ui_DialogProjectName





''' Klasse die den Dialog zum editieren des Projekt Name erstellt '''        
class DialogProjectName(QMainWindow, Ui_DialogProjectName):
    def __init__(self, main_window):
        self.main_window = main_window
        super(DialogProjectName, self).__init__()
        self.setupUi(self)
        self.pushButton_Abbrechen.clicked.connect(self.close)
        self.pushButton_OK.clicked.connect(self.okClicked)


    def okClicked(self):
        self.changeProjectName()
        self.close()


    def changeProjectName(self):
        self.lineEditProjektName.textChanged.connect(self.main_window.labelProjektname.setText(self.lineEditProjektName.text()))
        '''TODO: 
           Projekname musss zwischengespeichert werden und bei Programmstart wieder geladen werden
           - Dazu muss das Projektname in einer Datei gespeichert werden
        '''
        



''' Klasse die das Hauptfenster erzeugt '''
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        'projektname'
        self.toolButtonProjektname.clicked.connect(self.openDialogProjectName)
        self.dialogProjectName = DialogProjectName(self)

        icon = QIcon("resources/images/gear-2-64.png")
        self.toolButtonProjektname.setIcon(icon)




    'Methode zum öffnen des Dialogs zum editieren des Projektnamens '
    def openDialogProjectName(self):
        self.dialogProjectName.show()




''' Hauptprogramm '''
if __name__ == "__main__":
    print(os.getcwd())
   
   
    app = QApplication(sys.argv)
    main_Window = MainWindow()
    main_Window.show()
 
    sys.exit(app.exec())

