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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QLCDNumber,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

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
        self.labelProjektname.setGeometry(QRect(0, 10, 1280, 90))
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
        icon.addFile(u"../../../.designer/resources/images/gear-42.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonProjektname.setIcon(icon)
        self.pushButtonProjektname.setIconSize(QSize(42, 42))
        self.pushButtonProjektname.setCheckable(True)
        self.pushButtonProjektname.setAutoDefault(False)
        self.pushButtonProjektname.setFlat(True)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(324, 180, 631, 152))
        self.m2formLayout = QFormLayout(self.layoutWidget)
        self.m2formLayout.setObjectName(u"m2formLayout")
        self.m2formLayout.setContentsMargins(0, 0, 0, 0)
        self.m2lcdNumber = QLCDNumber(self.layoutWidget)
        self.m2lcdNumber.setObjectName(u"m2lcdNumber")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.m2lcdNumber.sizePolicy().hasHeightForWidth())
        self.m2lcdNumber.setSizePolicy(sizePolicy2)
        self.m2lcdNumber.setMinimumSize(QSize(500, 150))
        self.m2lcdNumber.setSmallDecimalPoint(True)
        self.m2lcdNumber.setDigitCount(7)
        self.m2lcdNumber.setProperty("value", 1220.220000000000027)

        self.m2formLayout.setWidget(0, QFormLayout.LabelRole, self.m2lcdNumber)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.m2pushButton = QPushButton(self.layoutWidget)
        self.m2pushButton.setObjectName(u"m2pushButton")

        self.verticalLayout.addWidget(self.m2pushButton)

        self.m2label = QLabel(self.layoutWidget)
        self.m2label.setObjectName(u"m2label")
        font2 = QFont()
        font2.setFamilies([u"Segoe Fluent Icons"])
        font2.setPointSize(14)
        self.m2label.setFont(font2)
        self.m2label.setFrameShape(QFrame.NoFrame)
        self.m2label.setTextFormat(Qt.RichText)
        self.m2label.setScaledContents(False)
        self.m2label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout.addWidget(self.m2label)


        self.m2formLayout.setLayout(0, QFormLayout.FieldRole, self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButtonProjektname.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelProjektname.setText(QCoreApplication.translate("MainWindow", u"Hamburg RB0, Tag 1", None))
        self.m2pushButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.m2label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:48pt;\">m</span><span style=\" font-size:48pt; vertical-align:super;\">2</span></p></body></html>", None))
    # retranslateUi

