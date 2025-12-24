from PySide6.QtWidgets import QApplication, QWidget, QCheckBox, QVBoxLayout, QPushButton
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        cb = QCheckBox('111')
        cb.stateChanged.connect(self.showName)
        cb.setTristate(False) #三狀態

        btn = QPushButton('get state')
        btn.clicked.connect(lambda: print(cb.isChecked()))

        mainlayout = QVBoxLayout()
        mainlayout.addWidget(cb)
        mainlayout.addWidget(btn)
        self.setLayout(mainlayout)

    def showName(self, name):
        print(name)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()