from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFontDialog, QColorDialog, QTextEdit, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.edit = QTextEdit()

        self.btn1 = QPushButton('select font')
        self.btn1.clicked.connect(self.selectFont)
        self.btn2 = QPushButton('select color')
        self.btn2.clicked.connect(self.electColor)
        
        self.mainLayout = QVBoxLayout()
        self.btnLayout = QHBoxLayout()
        self.btnLayout.addWidget(self.btn1)
        self.btnLayout.addWidget(self.btn2)
        self.mainLayout.addWidget(self.edit)
        self.mainLayout.addLayout(self.btnLayout)
        self.setLayout(self.mainLayout)

    def selectFont(self):
        ok, font = QFontDialog.getFont()
        if not ok:
            return
        self.edit.setFont(font)

    def electColor(self):
        color = QColorDialog.getColor()
        self.edit.setTextColor(color)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()