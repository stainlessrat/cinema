import sys

from PyQt5.QtWidgets import QApplication

from UI.cinima_window import Window


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
