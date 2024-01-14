from PySide6.QtCore import QSettings


''' Konfigurationsdatei laden '''
conf = QSettings('./config.ini', QSettings.IniFormat)