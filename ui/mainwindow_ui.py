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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.groupBoxProjektname = QGroupBox(self.centralwidget)
        self.groupBoxProjektname.setObjectName(u"groupBoxProjektname")
        self.groupBoxProjektname.setGeometry(QRect(0, 0, 1280, 100))
        self.groupBoxProjektname.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.groupBoxProjektname.setAutoFillBackground(False)
        self.groupBoxProjektname.setAlignment(Qt.AlignCenter)
        self.groupBoxProjektname.setFlat(True)
        self.labelProjektname = QLabel(self.groupBoxProjektname)
        self.labelProjektname.setObjectName(u"labelProjektname")
        self.labelProjektname.setGeometry(QRect(0, 0, 1281, 91))
        font = QFont()
        font.setPointSize(48)
        self.labelProjektname.setFont(font)
        self.labelProjektname.setAlignment(Qt.AlignCenter)
        self.pushButtonProjektname = QPushButton(self.groupBoxProjektname)
        self.pushButtonProjektname.setObjectName(u"pushButtonProjektname")
        self.pushButtonProjektname.setGeometry(QRect(1210, 30, 48, 48))
        self.pushButtonProjektname.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u"../resources/images/gear-2-multi-size.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonProjektname.setIcon(icon)
        self.pushButtonProjektname.setIconSize(QSize(42, 42))
        self.pushButtonProjektname.setFlat(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBoxProjektname.setTitle("")
        self.labelProjektname.setText(QCoreApplication.translate("MainWindow", u"Hamburg RB0, Tag 1", None))
        self.pushButtonProjektname.setText("")
    # retranslateUi

