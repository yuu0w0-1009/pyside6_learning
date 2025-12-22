from PySide6.QtWidgets import QApplication as qap
from PySide6.QtWidgets import QMainWindow as qmw

class MyWindow(qmw):
    def __init__(self):
        super().__init__()

if __name__ == '__main__':
    app = qap([])
    window = MyWindow()
    window.show()
    app.exec()