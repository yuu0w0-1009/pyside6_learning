# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RadioButton.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QRadioButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(202, 44)
        icon = QIcon(QIcon.fromTheme(u"appointment-new"))
        Form.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButtonA = QRadioButton(Form)
        self.radioButtonA.setObjectName(u"radioButtonA")

        self.horizontalLayout.addWidget(self.radioButtonA)

        self.radioButtonB = QRadioButton(Form)
        self.radioButtonB.setObjectName(u"radioButtonB")

        self.horizontalLayout.addWidget(self.radioButtonB)

        self.radioButtonC = QRadioButton(Form)
        self.radioButtonC.setObjectName(u"radioButtonC")

        self.horizontalLayout.addWidget(self.radioButtonC)

        self.radioButtonD = QRadioButton(Form)
        self.radioButtonD.setObjectName(u"radioButtonD")

        self.horizontalLayout.addWidget(self.radioButtonD)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"QRadioButton", None))
        self.radioButtonA.setText(QCoreApplication.translate("Form", u"A", None))
        self.radioButtonB.setText(QCoreApplication.translate("Form", u"B", None))
        self.radioButtonC.setText(QCoreApplication.translate("Form", u"C", None))
        self.radioButtonD.setText(QCoreApplication.translate("Form", u"D", None))
    # retranslateUi

