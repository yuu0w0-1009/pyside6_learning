# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project01_Login.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(500, 500)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.AddressBookNew))
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(0.950000000000000)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(190, 100, 300, 80))
        font = QFont()
        font.setFamilies([u"\u5c0f\u8cf4\u5b57\u9ad4 \u7b49\u5bec SC"])
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 100, 150, 80))
        font1 = QFont()
        font1.setFamilies([u"\u5c0f\u8cf4\u5b57\u9ad4 \u7b49\u5bec SC"])
        font1.setPointSize(25)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(190, 300, 300, 80))
        self.lineEdit_2.setFont(font)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 300, 150, 80))
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(200, 425, 90, 30))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u767b\u9304\u6846", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u8acb\u8f38\u5165\u5e33\u865f", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5e33\u865f", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"\u8acb\u8f38\u5165\u5bc6\u78bc", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5bc6\u78bc", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"login", None))
    # retranslateUi

