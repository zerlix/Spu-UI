# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogProjectName.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_DialogProjectName(object):
    def setupUi(self, DialogProjectName):
        if not DialogProjectName.objectName():
            DialogProjectName.setObjectName(u"DialogProjectName")
        DialogProjectName.resize(798, 164)
        self.label = QLabel(DialogProjectName)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 761, 31))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.lineEditProjektName = QLineEdit(DialogProjectName)
        self.lineEditProjektName.setObjectName(u"lineEditProjektName")
        self.lineEditProjektName.setGeometry(QRect(50, 60, 691, 41))
        self.pushButton_OK = QPushButton(DialogProjectName)
        self.pushButton_OK.setObjectName(u"pushButton_OK")
        self.pushButton_OK.setGeometry(QRect(570, 120, 75, 24))
        self.pushButton_Abbrechen = QPushButton(DialogProjectName)
        self.pushButton_Abbrechen.setObjectName(u"pushButton_Abbrechen")
        self.pushButton_Abbrechen.setGeometry(QRect(660, 120, 75, 24))

        self.retranslateUi(DialogProjectName)

        QMetaObject.connectSlotsByName(DialogProjectName)
    # setupUi

    def retranslateUi(self, DialogProjectName):
        DialogProjectName.setWindowTitle(QCoreApplication.translate("DialogProjectName", u"Projekt Name \u00e4ndern", None))
        self.label.setText(QCoreApplication.translate("DialogProjectName", u"Geben Sie eine Projektbeschreibung an.", None))
        self.pushButton_OK.setText(QCoreApplication.translate("DialogProjectName", u"OK", None))
        self.pushButton_Abbrechen.setText(QCoreApplication.translate("DialogProjectName", u"Abbrechen", None))
    # retranslateUi

