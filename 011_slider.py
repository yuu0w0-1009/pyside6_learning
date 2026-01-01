from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        slider = QSlider(Qt.Orientation.Horizontal)
        slider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        slider.setTickInterval(10)
        slider.setRange(0,100)

        slider.valueChanged.connect(lambda: print(f'{slider.value():d}'))

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(slider)
        self.setLayout(self.mainLayout)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()