from PySide6.QtWidgets import QApplication, QWidget
from Ui_trans import Ui_Form

class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #字典
        self.lengthVar = {'公分':1, '公尺':100, '公里':1000, '英里':160934.4}
        self.weigthVar = {'公克':1, '公斤':1000, '英鎊':453.5924}

        self.TypeDict = {'長度':self.lengthVar, '質量':self.weigthVar}

        self.ComboBoxSelect.addItems(self.TypeDict.keys())
        self.ComboBoxInput1.addItems(self.lengthVar.keys())
        self.ComboBoxInput2.addItems(self.lengthVar.keys())

        self.bind()

    def bind(self):
        self.ComboBoxSelect.currentTextChanged.connect(self.typeChange)
        self.pushButtonCalc.clicked.connect(self.calc)

    def calc(self):
        bigType = self.ComboBoxSelect.currentText()

        value = self.LineEditInput1.text()
        if value == '':
            return
        
        nowType = self.ComboBoxInput1.currentText()
        nextType = self.ComboBoxInput2.currentText()

        AA = float(value) * self.TypeDict[bigType][nowType]
        result = AA / self.TypeDict[bigType][nextType] 

        self.LabelOutput1.setText(f'{value} {nowType} =')
        self.LabelOutput2.setText(f'{result} {nextType}')
        self.LineEditInput2.setText(str(result))

    def typeChange(self, text):
        self.ComboBoxInput1.clear()
        self.ComboBoxInput2.clear()

        self.ComboBoxInput1.addItems(self.TypeDict[text].keys())
        self.ComboBoxInput2.addItems(self.TypeDict[text].keys())

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()