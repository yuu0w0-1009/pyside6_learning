from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPlainTextEdit, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        textedit = QPlainTextEdit()
        textedit.appendPlainText('1')
        textedit.setReadOnly(1)

        btn = QPushButton()
        btn.setText('+1')
        btn.clicked.connect(lambda: textedit.appendPlainText('+1'))

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(textedit)
        self.mainLayout.addWidget(btn)
        self.setLayout(self.mainLayout)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()