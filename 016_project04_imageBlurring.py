from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QSlider, QFileDialog, QLabel, QPushButton
from PySide6.QtCore import Qt
from PIL import Image, ImageFilter, ImageQt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.btn = QPushButton('import img')

        self.showImg = QLabel()

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.slider.setTickInterval(4)
        self.slider.setRange(0,20)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.btn)
        self.mainLayout.addWidget(self.showImg)
        self.mainLayout.addWidget(self.slider)
        self.setLayout(self.mainLayout)
        self.bind()

    def bind(self):
        self.btn.clicked.connect(self.getImg)
        self.slider.valueChanged.connect(self.sliderChange)

    def getImg(self):
        self.img = Image.open(QFileDialog.getOpenFileName(self, 'select picture', './', 'picture(*.png *.jpg)')[0])
        self.showImg.setPixmap(ImageQt.toqpixmap(self.img))

    def sliderChange(self, value):
        self.blurImg = self.img.filter(ImageFilter.GaussianBlur(value))
        self.showImg.setPixmap(ImageQt.toqpixmap(self.blurImg))


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()