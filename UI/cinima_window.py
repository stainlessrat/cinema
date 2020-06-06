from PyQt5.QtWidgets import QWidget, QPushButton, \
    QHBoxLayout, QVBoxLayout, QLabel, QSlider, QStyle, \
    QSizePolicy
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cinema")
        self.setGeometry(350, 100, 700, 500)
        self.setWindowIcon(QIcon('images.png'))

        p = self.palette()
        p.setColor(QPalette.Window, Qt.darkGray)
        self.setPalette(p)

        self.init_ui()

        self.show()

    def init_ui(self):
        # create media player object
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        # create videowidget object
        videowidget = QVideoWidget()

        # create open button
        open_btn = QPushButton('Open Video')

        # create button for playing
        self.play_btn = QPushButton()
        self.play_btn.setEnabled(False)
        self.play_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

        # create slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,0)

        # create label
        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        # create hbox layout
        hbox_layout = QHBoxLayout()
        hbox_layout.setContentsMargins(0,0,0,0)

        # set widgets to the nbox layout
        hbox_layout.addWidget(open_btn)
        hbox_layout.addWidget(self.play_btn)
        hbox_layout.addWidget(self.slider)

        # create vbox layout
        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(videowidget)
        vbox_layout.addLayout(hbox_layout)
        vbox_layout.addWidget(self.label)

        self.setLayout(vbox_layout)