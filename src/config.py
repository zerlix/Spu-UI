from PySide6.QtCore import QSettings


''' Konfigurationsdatei laden '''
conf = QSettings('./config.ini', QSettings.IniFormat)



'''Stylesheet aus Dateien zusammenführen und anwenden'''
def merge_Stylesheet():
    stylesheet = ''
    theme = conf.value('theme')

    'Stylesheets einlesen' 
    with open('./resources/styles/styles.qss', 'r') as f:
        cssMain = f.read()
    
    with open('./resources/styles/'+theme+'.qss', 'r') as f:
       cssTheme = f.read()
    
    'Beide Stylesheets zusammenführen'
    stylesheet = cssMain + '\n' + cssTheme
    return stylesheet
