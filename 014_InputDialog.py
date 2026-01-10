from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QPlainTextEdit, QInputDialog, QLineEdit

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.btnInt = QPushButton('get Int')
        self.btnInt.clicked.connect(self.btnGetInt)

        self.btnDouble = QPushButton('get Double')
        self.btnDouble.clicked.connect(self.btnGetDouble)

        self.btnItem = QPushButton('get Item')
        self.btnItem.clicked.connect(self.btnGetItem)

        self.btnText = QPushButton('get Text')
        self.btnText.clicked.connect(self.btnGetText)

        self.btnStr = QPushButton('get Str')
        self.btnStr.clicked.connect(self.btnGetStr)

        self.textedit = QPlainTextEdit()
        self.textedit.setReadOnly(1)

        self.mainLayout = QVBoxLayout()
        self.btnLayout = QHBoxLayout()
        self.btnLayout.addWidget(self.btnInt)
        self.btnLayout.addWidget(self.btnDouble)
        self.btnLayout.addWidget(self.btnItem)
        self.btnLayout.addWidget(self.btnText)
        self.btnLayout.addWidget(self.btnStr)
        self.mainLayout.addWidget(self.textedit)
        self.mainLayout.addLayout(self.btnLayout)
        self.setLayout(self.mainLayout)

    def btnGetInt(self):
        self.textedit.appendPlainText('Int clicked!')
                                                            #初始值, min, max,step=一次給值
        replay, ok = QInputDialog.getInt(self, '標題', '內容', 0, 0, 100, step=1)
        if ok:
            self.textedit.appendPlainText(f'{replay:d}')

    def btnGetDouble(self):
        self.textedit.appendPlainText('Double clicked!')
                                                                #初始值, min, max,顯示位數,step=一次給值
        replay, ok = QInputDialog.getDouble(self, '標題', '內容', 0, 0, 100, 3, step=0.05)
        if ok:
            self.textedit.appendPlainText(f'{replay:.3f}')
         
    def btnGetItem(self):
        self.textedit.appendPlainText('Item clicked!')
                                                                #值, 初始值, editable(可編輯)
        replay, ok = QInputDialog.getItem(self, '標題', '內容', ['a', 'b', 'c'], 2, 0)
        if ok:
            self.textedit.appendPlainText(f'{replay:s}')

    def btnGetText(self):
        self.textedit.appendPlainText('Text clicked!')
        replay, ok = QInputDialog.getText(self, '標題', '內容', QLineEdit.EchoMode.Normal, '默認值')
        if ok:
            self.textedit.appendPlainText(f'{replay:s}')

    def btnGetStr(self):
        self.textedit.appendPlainText('Str clicked!')
        replay, ok = QInputDialog.getMultiLineText(self, '標題', '內容')
        if ok:
            self.textedit.appendPlainText(f'{replay}')

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()