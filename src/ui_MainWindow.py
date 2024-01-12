# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1280, 800))
        MainWindow.setMaximumSize(QSize(1280, 800))
        font = QFont()
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.labelProjektname = QLabel(self.centralwidget)
        self.labelProjektname.setObjectName(u"labelProjektname")
        self.labelProjektname.setGeometry(QRect(0, 10, 1281, 91))
        font1 = QFont()
        font1.setPointSize(48)
        self.labelProjektname.setFont(font1)
        self.labelProjektname.setAlignment(Qt.AlignCenter)
        self.pushButtonProjektname = QPushButton(self.centralwidget)
        self.pushButtonProjektname.setObjectName(u"pushButtonProjektname")
        self.pushButtonProjektname.setGeometry(QRect(1200, 20, 64, 64))
        self.pushButtonProjektname.setFocusPolicy(Qt.ClickFocus)
        self.pushButtonProjektname.setAutoFillBackground(False)
        self.pushButtonProjektname.setText(u"")
        icon = QIcon()
        icon.addFile(u"../resources/images/gear-42.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonProjektname.setIcon(icon)
        self.pushButtonProjektname.setIconSize(QSize(42, 42))
        self.pushButtonProjektname.setCheckable(True)
        self.pushButtonProjektname.setAutoDefault(False)
        self.pushButtonProjektname.setFlat(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButtonProjektname.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelProjektname.setText(QCoreApplication.translate("MainWindow", u"Hamburg RB0, Tag 1", None))
    # retranslateUi

