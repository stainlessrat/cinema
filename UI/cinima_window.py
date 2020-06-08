from PyQt5.QtWidgets import QWidget, QPushButton, \
    QHBoxLayout, QVBoxLayout, QLabel, QSlider, QStyle, \
    QSizePolicy, QFileDialog
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl


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
        open_btn.clicked.connect(self.open_file)

        # create button for playing
        self.play_btn = QPushButton()
        self.play_btn.setEnabled(False)
        self.play_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.play_btn.clicked.connect(self.play_video)

        # create slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_position)

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

        self.mediaPlayer.setVideoOutput(videowidget)

        # media player signals
        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")

        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.play_btn.setEnabled(True)

    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediastate_changed(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.play_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.play_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def position_changed(self, position):
        self.slider.setValue(position)

    def duration_changed(self, duration):
        self.slider.setRange(0, duration)

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)

    def handle_errors(self):
        self.play_btn.setEnabled(False)
        self.label.setText('Error: ' + self.mediaPlayer.errorString())
