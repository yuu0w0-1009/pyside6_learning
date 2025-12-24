from PySide6.QtWidgets import QApplication as qap
from PySide6.QtWidgets import QWidget as qwg
from Ui_project01_Login import Ui_Form

class MyWindow(qwg):
    def __init__(self):
        super().__init__()
        self.Ui = Ui_Form()
        self.Ui.setupUi(self)

if __name__ == '__main__':
    app = qap([])
    window = MyWindow()
    window.show()
    app.exec()