# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLCDNumber, QMainWindow,
    QSizePolicy, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 800)
        MainWindow.setMinimumSize(QSize(1280, 800))
        MainWindow.setMaximumSize(QSize(1280, 800))
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(90, 570, 241, 91))
        self.lcdNumber.setFrameShape(QFrame.StyledPanel)
        self.lcdNumber.setFrameShadow(QFrame.Plain)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setProperty("value", 12.199999999999999)
        self.lcdNumber_2 = QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setGeometry(QRect(520, 570, 241, 91))
        self.lcdNumber_2.setFrameShape(QFrame.StyledPanel)
        self.lcdNumber_2.setFrameShadow(QFrame.Plain)
        self.lcdNumber_2.setSmallDecimalPoint(False)
        self.lcdNumber_2.setProperty("value", 12.199999999999999)
        self.lcdNumber_3 = QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setObjectName(u"lcdNumber_3")
        self.lcdNumber_3.setGeometry(QRect(940, 570, 241, 91))
        self.lcdNumber_3.setFrameShape(QFrame.StyledPanel)
        self.lcdNumber_3.setFrameShadow(QFrame.Plain)
        self.lcdNumber_3.setSmallDecimalPoint(False)
        self.lcdNumber_3.setProperty("value", 12.199999999999999)
        self.lcdNumber_4 = QLCDNumber(self.centralwidget)
        self.lcdNumber_4.setObjectName(u"lcdNumber_4")
        self.lcdNumber_4.setGeometry(QRect(90, 350, 241, 91))
        self.lcdNumber_4.setFrameShape(QFrame.StyledPanel)
        self.lcdNumber_4.setSmallDecimalPoint(False)
        self.lcdNumber_4.setProperty("value", 12.199999999999999)
        self.lcdNumber_5 = QLCDNumber(self.centralwidget)
        self.lcdNumber_5.setObjectName(u"lcdNumber_5")
        self.lcdNumber_5.setGeometry(QRect(520, 360, 241, 91))
        self.lcdNumber_5.setFrameShape(QFrame.StyledPanel)
        self.lcdNumber_5.setFrameShadow(QFrame.Plain)
        self.lcdNumber_5.setSmallDecimalPoint(False)
        self.lcdNumber_5.setProperty("value", 12.199999999999999)
        self.lcdNumber_6 = QLCDNumber(self.centralwidget)
        self.lcdNumber_6.setObjectName(u"lcdNumber_6")
        self.lcdNumber_6.setGeometry(QRect(940, 360, 241, 91))
        self.lcdNumber_6.setFrameShape(QFrame.StyledPanel)
        self.lcdNumber_6.setFrameShadow(QFrame.Plain)
        self.lcdNumber_6.setSmallDecimalPoint(False)
        self.lcdNumber_6.setProperty("value", 12.199999999999999)
        self.lcdNumber_7 = QLCDNumber(self.centralwidget)
        self.lcdNumber_7.setObjectName(u"lcdNumber_7")
        self.lcdNumber_7.setGeometry(QRect(330, 160, 621, 141))
        self.lcdNumber_7.setFrameShape(QFrame.StyledPanel)
        self.lcdNumber_7.setFrameShadow(QFrame.Plain)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(400, 30, 511, 71))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

