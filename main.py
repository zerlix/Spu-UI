# main.py
import sys
import os

# Setzen Sie QT_IM_MODULE auf 'qtvirtualkeyboard'
os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"

from PySide6.QtCore import Qt 
from PySide6.QtWidgets import QApplication, QMainWindow
from src.MainWindow_ui import Ui_MainWindow
from src.DialogProjectName_ui import Ui_DialogProjectName




''' Klasse die den Dialog zum editieren des Projekt Name erstellt '''        
class DialogProjectName(QMainWindow, Ui_DialogProjectName):
    def __init__(self):
        super(DialogProjectName, self).__init__()
        self.setupUi(self)
        self.pushButton_Abbrechen.clicked.connect(self.close)
        self.pushButton_OK.clicked.connect(self.changeProjectName)


    def changeProjectName(self):
        pass



''' Klasse die das Hauptfenster erzeugt '''
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.toolButtonProjektname.clicked.connect(self.openDialogProjectName)


    'Methode zum öffnen des Dialogs zum editieren des Projektnamens '
    def openDialogProjectName(self):
        self.dialogProjectName = DialogProjectName()
        self.dialogProjectName.show()





''' Hauptprogramm '''
if __name__ == "__main__":
    # Mainwindow
    app = QApplication(sys.argv)

    main_Window = MainWindow()
    main_Window.show()
    widget_EditProjectName = DialogProjectName()
    
    

    sys.exit(app.exec())

