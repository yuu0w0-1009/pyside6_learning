from PySide6.QtWidgets import QApplication as qap
from PySide6.QtWidgets import QWidget as qwg
from Ui_project01_Login import Ui_Form

class MyWindow(qwg, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.loginFuc)

    def loginFuc(self):
        account = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if account == '123' and password == '456':
            print("登陸成功")
        else:
            print("登陸失敗")


if __name__ == '__main__':
    app = qap([])
    window = MyWindow()
    window.show()
    app.exec()