import random
import sys

from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow

SCREEN_SIZE = [515, 365]


class YellowCircle(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag = False
        self.setWindowTitle("Желтые окружности")
        self.buttonYellow.clicked.connect(self.draw)

    def draw(self):
        self.figure = "circle"
        self.flag = True
        self.size = random.randint(10, 301)
        self.color = QColor('yellow')
        self.update()

    def paintEvent(self, event):
        if self.flag:
            painter = QPainter()
            painter.begin(self)
            painter.setBrush(self.color)
            self.x, self.y = random.randint(0, SCREEN_SIZE[0] - 100), random.randint(0, SCREEN_SIZE[1] - 200)
            if self.figure == "circle":
                painter.drawEllipse(self.x, self.y, self.size, self.size)
            painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    y_c = YellowCircle()
    y_c.show()
    sys.exit(app.exec())
