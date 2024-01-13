from src.ui_DialogProjectName import Ui_DialogProjectName
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt


class DialogProjectName(QMainWindow, Ui_DialogProjectName):
    ''' Klasse die den Dialog zum editieren des Projekt Name erstellt '''    
    def __init__(self, main_window):
        self.main_window = main_window
        super(DialogProjectName, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        
        'Buttons connecten'
        self.pushButton_Abbrechen.clicked.connect(self.close)
        self.pushButton_OK.clicked.connect(self.okClicked)

        ''' TODO: 
            - Positionierung des Dialogfenster arbeitet nicht richtig
        main_x = main_window.pos().x()
        main_y = main_window.pos().y() 
        'Berechne x-Position'
        x = main_x + (main_window.width() - self.width()) / 2  
        'Setze y-Position'
        y = main_y + 20
        self.move(x, y)
        '''

    ' Ok wurde gedrückt'
    def okClicked(self):
        self.changeProjectName()
        self.close()

    'ändert den Projektnamen'
    def changeProjectName(self):
        self.lineEditProjektName.textChanged.connect(self.main_window.labelProjektname.setText(self.lineEditProjektName.text()))
        '''TODO: 
           - Projekname musss zwischengespeichert werden und bei Programmstart wieder geladen werden
        '''
      
