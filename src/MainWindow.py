from src.ui_MainWindow import Ui_MainWindow
from src.DialogProjectName import DialogProjectName
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt



''' Klasse die das Hauptfenster erzeugt '''
class MainWindow(QMainWindow, Ui_MainWindow):
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