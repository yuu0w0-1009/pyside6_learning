from PySide6.QtWidgets import QApplication as qap
from PySide6.QtWidgets import QWidget as qwg

class MyWindow(qwg):
    def __init__(self):
        super().__init__()

if __name__ == '__main__':
    app = qap([])
    window = MyWindow()
    window.show()
    app.exec()