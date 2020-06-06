from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cinema")
        self.setGeometry(350, 100, 700, 500)
        self.setWindowIcon(QIcon('images.png'))

        self.show()


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
