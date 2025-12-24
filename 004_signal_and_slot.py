from PySide6.QtWidgets import QApplication as qap
from PySide6.QtWidgets import QWidget as qwg
from PySide6.QtWidgets import QPushButton as qpb
from PySide6.QtWidgets import QLabel as qlb
from PySide6.QtWidgets import QLineEdit as qle
from PySide6.QtCore import Qt

class MyWindow(qwg):
    def __init__(self):
        super().__init__()

        btn = qpb(self)
        btn.clicked.connect(self.hello) #signal 
        btn.setText('按鈕')
        btn.setGeometry(100,100,200,100)
        # btn.setToolTip('666')
        

        # lb = qlb(self)
        # lb.setText('標籤')
        # lb.setGeometry(100,200,200,100)
        # lb.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # line = qle(self)
        # line.setGeometry(100,300,200,100)
        # line.setMaxLength(5)
        # line.setPlaceholderText('請輸入內容')

    def hello(self): #slot
        print("hello world")

if __name__ == '__main__':
    app = qap([])
    window = MyWindow()
    window.show()
    app.exec()