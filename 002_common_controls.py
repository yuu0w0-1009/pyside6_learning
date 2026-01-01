from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        btn = QPushButton(self)
        btn.setText('按鈕')
        btn.setGeometry(100,100,200,100)
        btn.setToolTip('666')

        lb = QLabel(self)
        lb.setText('標籤')
        lb.setGeometry(100,200,200,100)
        lb.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        line = QLineEdit(self)
        line.setGeometry(100,300,200,100)
        line.setMaxLength(5)
        line.setPlaceholderText('請輸入內容')

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()