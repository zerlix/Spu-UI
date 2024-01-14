from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import Qt
from src.ui_DialogProjectName import Ui_DialogProjectName
from src.config import conf


class DialogProjectName(QMainWindow, Ui_DialogProjectName):
    '''Klasse die den Dialog zum editieren des Projekt Name erstellt'''    
    def __init__(self, main_window):
        self.main_window = main_window
        super(DialogProjectName, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        
        '''Buttons connecten'''
        self.pushButton_Abbrechen.clicked.connect(self.close)
        self.pushButton_OK.clicked.connect(self.okClicked)

        ''' Bildschirmauflösung des Primärmonitors feststellen um das Dialogfenster an den Bildschirm zu positionieren'''
        screens = QApplication.screens()
        screen = screens[0]
        screen_geometry = screen.availableGeometry()
        screen_x = screen_geometry.x()
        screen_y = screen_geometry.y()
        # Berechnung der Position des Dialogfensters
        x = screen_x + (screen_geometry.width() - self.width()) / 2  
        y = screen_y + 20
        self.move(x, y)

    '''Ok wurde gedrückt'''
    def okClicked(self):
        self.changeProjectName()
        self.close()

    '''ändert den Projektnamen'''
    def changeProjectName(self):
        pName = self.lineEditProjektName.text()
        '''Speichern des Projektnamens in der Konfigurationsdatei'''
        conf.setValue('lastProject/name', pName)
        conf.sync()
        self.lineEditProjektName.textChanged.connect(self.main_window.labelProjektname.setText(pName))
