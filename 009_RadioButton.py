from PySide6.QtWidgets import QApplication, QWidget, QRadioButton, QButtonGroup
from UI.Ui_RadioButton import Ui_Form

class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.group = QButtonGroup(self)
        self.group.addButton(self.radioButtonA)
        self.group.addButton(self.radioButtonB)
        self.group.addButton(self.radioButtonC)
        self.group.addButton(self.radioButtonD)

        self.radioButtonA.clicked.connect(self.check)
        self.radioButtonB.clicked.connect(self.check)
        self.radioButtonC.clicked.connect(self.check)
        self.radioButtonD.clicked.connect(self.check)

    def check(self):
        item = self.group.checkedButton()
        if item != None:
            print(item.text())

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()