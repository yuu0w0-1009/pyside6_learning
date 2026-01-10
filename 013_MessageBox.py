from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox, QPlainTextEdit

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.btn = QPushButton('display')
        self.btn.clicked.connect(self.btnClicked)

        self.textedit = QPlainTextEdit()
        self.textedit.setReadOnly(1)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.textedit)
        self.mainLayout.addWidget(self.btn)
        self.setLayout(self.mainLayout)

    def btnClicked(self):
        self.textedit.appendPlainText('btn clicked!')

        replay = QMessageBox.information(self, '標題', '內容', QMessageBox.StandardButton.Ok|QMessageBox.StandardButton.No
                                         |QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Ok)
        if replay == QMessageBox.StandardButton.Ok:
            self.textedit.appendPlainText('clicked ok!')
        elif replay == QMessageBox.StandardButton.No:
            self.textedit.appendPlainText('clicked no!')
        elif replay == QMessageBox.StandardButton.Close:
            self.textedit.appendPlainText('clicked close!')

        # 順序為常用程度
        # QMessageBox.information(self,'標題','內容',按鈕,高亮按鈕) #i
        # QMessageBox.question(self,'標題','內容',按鈕,高亮按鈕) #?
        # QMessageBox.warning(self,'標題','內容',按鈕,高亮按鈕) #!
        # QMessageBox.critical(self,'標題','內容',按鈕,高亮按鈕) #X
        # QMessageBox.about(self,'標題','內容',按鈕,高亮按鈕)
        
if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()