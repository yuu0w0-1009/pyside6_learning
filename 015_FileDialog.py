from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPlainTextEdit, QPushButton, QFileDialog

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.textedit = QPlainTextEdit()
        self.textedit.setReadOnly(1)

        self.btn1 = QPushButton('選擇單個文件')
        self.btn1.clicked.connect(lambda:self.textedit.appendPlainText(str(QFileDialog.getOpenFileName(self, '選擇文件', '.', 'ALL Files (*);;py文件(*.py *.pyd)'))))
        #返回(path,過濾類型)

        self.btn2 = QPushButton('選擇多個文件')
        self.btn2.clicked.connect(lambda:self.textedit.appendPlainText(str(QFileDialog.getOpenFileNames(self, '選擇文件', '.', 'ALL Files (*);;py文件(*.py *.pyd)'))))
        #返回(path[],過濾類型)

        self.btn3 = QPushButton('選擇資料夾')
        self.btn3.clicked.connect(lambda:self.textedit.appendPlainText(str(QFileDialog.getExistingDirectory(self, '選擇資料夾', '.'))))
        #返回 path

        self.btn4 = QPushButton('save文件')
        self.btn4.clicked.connect(lambda:self.textedit.appendPlainText(str(QFileDialog.getSaveFileName(self,'選擇文件', '.', 'ALL Files (*);;py文件(*.py *.pyd)'))))
        #返回(path,過濾類型)

        self.mainLayout = QVBoxLayout()
        self.btnLayout = QHBoxLayout()
        self.btnLayout.addWidget(self.btn1)
        self.btnLayout.addWidget(self.btn2)
        self.btnLayout.addWidget(self.btn3)
        self.btnLayout.addWidget(self.btn4)
        self.mainLayout.addWidget(self.textedit)
        self.mainLayout.addLayout(self.btnLayout)
        self.setLayout(self.mainLayout)



if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()