from PySide6.QtWidgets import QApplication as qap
from PySide6.QtWidgets import QMainWindow as qmw
from PySide6.QtWidgets import QWidget as qwg
from Ui_project02_calculator import Ui_Form

class MyWindow(qwg, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

if __name__ == '__main__':
    app = qap([])
    window = MyWindow()
    window.show()
    app.exec()