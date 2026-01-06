from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                               QPushButton, QPlainTextEdit, QLineEdit, QComboBox, QCheckBox, 
                               QButtonGroup, QRadioButton, QSlider)
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.btn1 = QPushButton()
        self.btn1.setText('按鈕')
        self.btnClear = QPushButton()
        self.btnClear.setText('Clear')

        self.lbl = QLabel()
        self.lbl.setText('課程總結')
        self.lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.textedit = QPlainTextEdit()
        self.textedit.setReadOnly(1)

        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText('請輸入內容')
        self.lineEdit.setEchoMode(QLineEdit.EchoMode.Normal)
        
        self.cbb = QComboBox()
        self.cbb.setPlaceholderText('請選擇')
        self.cbb.addItems(['a', 'b', 'c'])
        
        self.ckb1 = QCheckBox('#1')
        self.ckb1.setCheckable(1)
        
        self.ckb2 = QCheckBox('#2')
        self.ckb2.setCheckable(1)
        self.ckbTemp = [0]*2

        self.groupEng = QButtonGroup()
        self.rdbA = QRadioButton('A')
        self.rdbB = QRadioButton('B')
        self.groupEng.addButton(self.rdbA)
        self.groupEng.addButton(self.rdbB)

        self.groupNum = QButtonGroup()
        self.rdb1 = QRadioButton('1')
        self.rdb2 = QRadioButton('2')
        self.groupNum.addButton(self.rdb1)
        self.groupNum.addButton(self.rdb2)

        self.mainLayout = QVBoxLayout()

        self.ckbLayout = QHBoxLayout()
        self.ckbLayout.addWidget(self.ckb1)
        self.ckbLayout.addWidget(self.ckb2)

        self.rbdEngLayout = QHBoxLayout()
        self.rbdEngLayout.addWidget(self.rdbA)
        self.rbdEngLayout.addWidget(self.rdbB)

        self.rbdNumLayout = QHBoxLayout()
        self.rbdNumLayout.addWidget(self.rdb1)
        self.rbdNumLayout.addWidget(self.rdb2)

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.slider.setTickInterval(10)
        self.slider.setRange(0,100)

        self.mainLayout.addWidget(self.lbl)
        self.mainLayout.addWidget(self.textedit)
        self.mainLayout.addWidget(self.lineEdit)
        self.mainLayout.addWidget(self.cbb)
        self.mainLayout.addLayout(self.ckbLayout)
        self.mainLayout.addLayout(self.rbdEngLayout)
        self.mainLayout.addLayout(self.rbdNumLayout)
        self.mainLayout.addWidget(self.slider)
        self.mainLayout.addWidget(self.btn1)
        self.mainLayout.addWidget(self.btnClear)
        self.setLayout(self.mainLayout)
        self.bind()

    def bind(self):
        self.btn1.clicked.connect(self.btn1clicked)
        self.btnClear.clicked.connect(lambda: self.textedit.clear())
        self.lineEdit.returnPressed.connect(self.ledtreturnPressed)
        self.cbb.currentTextChanged.connect(self.cbbIndexChanhed)
        self.ckb1.stateChanged.connect(self.ckbChanged)
        self.ckb2.stateChanged.connect(self.ckbChanged)
        self.rdbA.clicked.connect(self.whichRdbClkedEng)
        self.rdbB.clicked.connect(self.whichRdbClkedEng)
        self.rdb1.clicked.connect(self.whichRdbClkedNum)
        self.rdb2.clicked.connect(self.whichRdbClkedNum)
        self.slider.valueChanged.connect(lambda: self.textedit.appendPlainText(f'{self.slider.value():d}'))


    def btn1clicked(self):
        self.textedit.appendPlainText('按鈕被點擊')

    def ledtreturnPressed(self):
        text = self.lineEdit.text()
        if(text!=''):
            self.textedit.appendPlainText(f'lineEdit輸入 : {text}')

    def cbbIndexChanhed(self, text):
        self.textedit.appendPlainText(f'ComboBox選擇 : {text}')

    def ckbChanged(self):
        c1 = self.ckb1.isChecked()
        c2 = self.ckb2.isChecked()
        if c1 == True and self.ckbTemp[0] == 0:
            self.textedit.appendPlainText(f'按下CheckBox1')
            self.ckbTemp[0] = 1
        if c2 == True and self.ckbTemp[1] == 0:
            self.textedit.appendPlainText(f'按下CheckBox2')
            self.ckbTemp[1] = 1
        if c1 == False and self.ckbTemp[0] == 1:
            self.textedit.appendPlainText(f'取消CheckBox1')
            self.ckbTemp[0] = 0
        if c2 == False and self.ckbTemp[1] == 1:
            self.textedit.appendPlainText(f'取消CheckBox2')
            self.ckbTemp[1] = 0

    def whichRdbClkedEng(self):
        self.textedit.appendPlainText(f'按下RadioButton {self.groupEng.checkedButton().text()} , 屬於groupEng')

    def whichRdbClkedNum(self):
        self.textedit.appendPlainText(f'按下RadioButton {self.groupNum.checkedButton().text()} , 屬於groupNum')


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()