from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QPlainTextEdit, QLineEdit, QComboBox, QCheckBox
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.btn1 = QPushButton()
        self.btn1.setText('按鈕')
        self.btn1.clicked.connect(self.btn1clicked)
        self.lbl = QLabel()
        self.lbl.setText('課程總結')
        self.lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.textedit = QPlainTextEdit()
        self.textedit.setReadOnly(1)
        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText('請輸入內容')
        self.lineEdit.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit.returnPressed.connect(self.ledtreturnPressed)
        self.cbb = QComboBox()
        self.cbb.setPlaceholderText('請選擇')
        self.cbb.addItems(['a', 'b', 'c'])
        self.cbb.currentTextChanged.connect(self.cbbIndexChanhed)
        self.ckb1 = QCheckBox('#1')
        self.ckb1.setCheckable(1)
        self.ckb1.stateChanged.connect(self.ckbChanged)
        self.ckb2 = QCheckBox('#2')
        self.ckb2.setCheckable(1)
        self.ckb2.stateChanged.connect(self.ckbChanged)
        self.ckbTemp = 0

        self.mainLayout = QVBoxLayout()
        self.ckbLayout = QHBoxLayout()
        self.ckbLayout.addWidget(self.ckb1)
        self.ckbLayout.addWidget(self.ckb2)
        self.mainLayout.addWidget(self.lbl)
        self.mainLayout.addWidget(self.textedit)
        self.mainLayout.addWidget(self.lineEdit)
        self.mainLayout.addWidget(self.cbb)
        self.mainLayout.addLayout(self.ckbLayout)
        self.mainLayout.addWidget(self.btn1)
        self.setLayout(self.mainLayout)

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
        if c1 == True and c2 == False and self.ckbTemp == 0:
            self.textedit.appendPlainText(f'按下CheckBox1')
            self.ckbTemp = 1
        elif c2 == True and c1 == False and self.ckbTemp == 0:
            self.textedit.appendPlainText(f'按下CheckBox2')
            self.ckbTemp = 2
        if c1 == True and self.ckbTemp == 2:
            self.textedit.appendPlainText(f'按下CheckBox1')
            self.ckbTemp = 1
            self.ckb2.setChecked(False)
        elif c2 == True and self.ckbTemp == 1:
            self.textedit.appendPlainText(f'按下CheckBox2')
            self.ckbTemp = 2
            self.ckb1.setChecked(False)
        if c1 == False and self.ckbTemp == 1:
            self.textedit.appendPlainText(f'取消CheckBox1')
        elif c2 == False and self.ckbTemp == 2:
            self.textedit.appendPlainText(f'取消CheckBox2')

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()