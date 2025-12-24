# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'trans.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 253)
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.LineEditInput1 = QLineEdit(Form)
        self.LineEditInput1.setObjectName(u"LineEditInput1")
        self.LineEditInput1.setMaximumSize(QSize(200, 16777215))
        font = QFont()
        font.setFamilies([u"\u5c0f\u8cf4\u5b57\u9ad4 \u7b49\u5bec SC"])
        font.setPointSize(20)
        self.LineEditInput1.setFont(font)

        self.gridLayout_2.addWidget(self.LineEditInput1, 5, 0, 1, 1)

        self.ComboBoxInput2 = QComboBox(Form)
        self.ComboBoxInput2.setObjectName(u"ComboBoxInput2")
        self.ComboBoxInput2.setFont(font)
        self.ComboBoxInput2.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)

        self.gridLayout_2.addWidget(self.ComboBoxInput2, 6, 1, 1, 1)

        self.ComboBoxInput1 = QComboBox(Form)
        self.ComboBoxInput1.setObjectName(u"ComboBoxInput1")
        self.ComboBoxInput1.setMinimumSize(QSize(180, 0))
        self.ComboBoxInput1.setMaximumSize(QSize(200, 16777215))
        self.ComboBoxInput1.setFont(font)

        self.gridLayout_2.addWidget(self.ComboBoxInput1, 5, 1, 1, 1)

        self.LineEditInput2 = QLineEdit(Form)
        self.LineEditInput2.setObjectName(u"LineEditInput2")
        self.LineEditInput2.setFont(font)

        self.gridLayout_2.addWidget(self.LineEditInput2, 6, 0, 1, 1)

        self.LabelOutput2 = QLabel(Form)
        self.LabelOutput2.setObjectName(u"LabelOutput2")
        self.LabelOutput2.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setFamilies([u"\u5c0f\u8cf4\u5b57\u9ad4 \u7b49\u5bec SC"])
        font1.setPointSize(28)
        self.LabelOutput2.setFont(font1)

        self.gridLayout_2.addWidget(self.LabelOutput2, 3, 0, 1, 2)

        self.LabelOutput1 = QLabel(Form)
        self.LabelOutput1.setObjectName(u"LabelOutput1")
        self.LabelOutput1.setEnabled(False)
        self.LabelOutput1.setMaximumSize(QSize(16777215, 30))
        self.LabelOutput1.setFont(font)
        self.LabelOutput1.setStyleSheet(u"color: rgb(112, 112, 112);")

        self.gridLayout_2.addWidget(self.LabelOutput1, 2, 0, 1, 2)

        self.ComboBoxSelect = QComboBox(Form)
        self.ComboBoxSelect.setObjectName(u"ComboBoxSelect")
        font2 = QFont()
        font2.setFamilies([u"\u5c0f\u8cf4\u5b57\u9ad4 \u7b49\u5bec SC"])
        font2.setPointSize(18)
        self.ComboBoxSelect.setFont(font2)
        self.ComboBoxSelect.setEditable(False)

        self.gridLayout_2.addWidget(self.ComboBoxSelect, 4, 0, 1, 2)

        self.pushButtonCalc = QPushButton(Form)
        self.pushButtonCalc.setObjectName(u"pushButtonCalc")

        self.gridLayout_2.addWidget(self.pushButtonCalc, 7, 0, 1, 2)


        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 0, 1, 1)


        self.retranslateUi(Form)

        self.ComboBoxInput2.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u55ae\u4f4d\u8f49\u63db\u5668", None))
        self.ComboBoxInput2.setCurrentText("")
        self.LabelOutput2.setText(QCoreApplication.translate("Form", u"0", None))
        self.LabelOutput1.setText(QCoreApplication.translate("Form", u"0", None))
        self.ComboBoxSelect.setCurrentText("")
        self.pushButtonCalc.setText(QCoreApplication.translate("Form", u"\u8a08\u7b97", None))
    # retranslateUi

