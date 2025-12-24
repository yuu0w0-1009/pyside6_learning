from PySide6.QtWidgets import QApplication as qap
from PySide6.QtWidgets import QMainWindow as qmw
from PySide6.QtWidgets import QWidget as qwg
from Ui_project02_calculator import Ui_Form

class MyWindow(qwg, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.result = ''

        self.bind()
    
    def bind(self):
        self.pushButton_0.clicked.connect(lambda: self.addnum('0'))
        self.pushButton_1.clicked.connect(lambda: self.addnum('1'))
        self.pushButton_2.clicked.connect(lambda: self.addnum('2'))
        self.pushButton_3.clicked.connect(lambda: self.addnum('3'))
        self.pushButton_4.clicked.connect(lambda: self.addnum('4'))
        self.pushButton_5.clicked.connect(lambda: self.addnum('5'))
        self.pushButton_6.clicked.connect(lambda: self.addnum('6'))
        self.pushButton_7.clicked.connect(lambda: self.addnum('7'))
        self.pushButton_8.clicked.connect(lambda: self.addnum('8'))
        self.pushButton_9.clicked.connect(lambda: self.addnum('9'))
        self.pushButton_add.clicked.connect(lambda: self.addnum('+'))
        self.pushButton_sub.clicked.connect(lambda: self.addnum('-'))
        self.pushButton_mul.clicked.connect(lambda: self.addnum('*'))
        self.pushButton_div.clicked.connect(lambda: self.addnum('/'))
        self.pushButton_decimal.clicked.connect(lambda: self.addnum('.'))
        self.pushButton_enter.clicked.connect(self.equal)
        self.pushButton_CE.clicked.connect(self.clear)
        self.pushButton_back.clicked.connect(self.back)

    def addnum(self, num):
        self.lineEdit.clear()
        self.result += num
        self.lineEdit.setText(self.result)

    def equal(self):
        self.numResult = eval(self.result)
        self.lineEdit.setText(str(self.numResult))

    def clear(self):
        self.result = ''
        self.lineEdit.clear()

    def back(self):
        self.result = self.result[:-1]
        self.lineEdit.setText(self.result)
        
if __name__ == '__main__':
    app = qap([])
    window = MyWindow()
    window.show()
    app.exec()