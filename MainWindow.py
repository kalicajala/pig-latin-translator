# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# class imports

# Qt Imports
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 185, 255)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 60, 241, 31))
        font = QFont()
        font.setFamilies([u"Sans Serif Collection"])
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.textbox = QLineEdit(self.centralwidget)
        self.textbox.setObjectName(u"textbox")
        self.textbox.setGeometry(QRect(20, 130, 331, 351))
        font1 = QFont()
        font1.setFamilies([u"Sans Serif Collection"])
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        self.textbox.setFont(font1)
        self.textbox.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	border-radius: 12px;\n"
"	font: 14pt \"Sans Serif Collection\";\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: rgb(255, 0, 213)\n"
"}")
        self.textbox.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.unchanged_text = QLineEdit(self.centralwidget)
        self.unchanged_text.setObjectName(u"unchanged_text")
        self.unchanged_text.setGeometry(QRect(450, 130, 331, 351))
        self.unchanged_text.setFont(font1)
        self.unchanged_text.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	border-radius: 12px;\n"
"	\n"
"	font: 14pt \"Sans Serif Collection\";\n"
"}")
        self.unchanged_text.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.unchanged_text.setReadOnly(True)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QRect(30, 500, 111, 41))
        font2 = QFont()
        font2.setFamilies([u"Sans Serif Collection"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 0, 255);\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: rgb(255, 85, 255);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	background-color: rgb(230, 0, 255);\n"
"}")
        self.pushButton.setCheckable(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Pig Latin Translator", None))
        self.textbox.setText("")
        self.textbox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"type something", None))
        self.unchanged_text.setText("")
        self.unchanged_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"this text will be read only", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
    # retranslateUi

    def __init__(self):
        # TODO: add the following connection functions

        # button pressed connected to displaying the translated text on unchanged_text (QLineEdit.Normal) (use setEchoMode)
        self.pushButton.clicked.connect(self.set_visible)
        # text changed connected to translate method in the sentence class (through the sentence object)
        self.textbox.textChanged.connect() # figure out the method
        # if isModified is true, sets the visibility of unchanged_text to false(QLineEdit.NoEcho)(use setEchoMode)
        self.textbox.isModified.connect(self.set_invisible)

    def set_visible(self):
        # when the button is pushed, the text will become visible
        self.unchanged_text.setEchoMode(QLineEdit.EchoMode.Normal)
    
    def set_invisible(self):
        # when the text is changed by the user, the translation becomes invisible again
        self.unchanged_text.setEchoMode(QLineEdit.EchoMode.NoEcho)
