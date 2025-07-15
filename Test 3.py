'''Youtube Audio Player'''
import sys
import threading
import requests

import pafy
import vlc
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QFont, QIcon, QPixmap, QImage
from PyQt5.QtWidgets import (QApplication, QDesktopWidget, QGridLayout, QLabel,
                             QLineEdit, QMainWindow, QWidget)

CAPTION_START = 'Start'
CAPTION_STOP = 'Stop'
ICON_SANDTIMER = 'yellow'
ICON_PASS = 'green'
ICON_FAIL = 'red'


class PoolingSignal(QObject):
    '''
    Initialize pooling signal
    '''
    pooling_signal = pyqtSignal()


class FetchingThread(threading.Thread):
    '''
    Worker thread processes network requests to fetch url from entered text
    '''

    def __init__(self, signal):
        '''
        init
        '''
        super().__init__()
        self.setDaemon(True)
        self._request_event = threading.Event()
        self._signal = signal
        self._examined_test = ''
        self._is_valid = False
        self._play_url = ''
        self._pafy = None
        self._image = None

    def fetch(self, examined_text):
        '''
        Fetching url from youtube id
        '''
        self._examined_test = examined_text
        self._request_event.set()

    def get_url(self):
        '''
        Returns fetched URL string
        '''
        return self._play_url

    def is_valid(self):
        '''
        Returns whether enterted test is valid youtube id
        '''
        return self._is_valid

    def get_pafy(self):
        '''
        Returns pafy object
        '''
        return self._pafy

    def get_image(self):
        '''
        Returns an image of video
        '''
        return self._image
        
    def run(self):
        '''
        Main thread's loop, where url is tried to fetched from youtube
        '''
        while True:
            if self._request_event.wait(0.5):
                self._is_valid = False
                self._pafy = None
                self._image = None
                try:
                    self._pafy = pafy.new(self._examined_test)
                    best = self._pafy.getbestaudio()
                    self._play_url = best.url
                    self._is_valid = True
                    self._image = QImage()
                    self._image.loadFromData(requests.get(self._pafy.thumb).content)
                except (ValueError, OSError):
                    pass
                
                self._signal.emit()
                self._request_event.clear()


class MyWindow(QMainWindow):
    '''
    UI window
    '''

    def __init__(self):
        super().__init__()
        #
        self.player = None  # player object
        self.play_url = ''  # URL string
        #
        self.p_s = PoolingSignal()
        self.p_s.pooling_signal.connect(self.pooling_fetched_data)

        self.f_th = FetchingThread(self.p_s.pooling_signal)
        self.f_th.start()
        
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle('YOUTUBE AUDIO PLAYER')
        self.setMinimumSize(480,720)

        # set window into center of screen
        rect = self.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        rect.moveCenter(center)
        self.move(rect.topLeft())

        self.init_ui()

    def init_ui(self):
        '''
        init of UI controls
        '''
        self.label = QLabel(self)
        self.label.setText('Paste youtube URL to play it in mp3 version')
        self.label.setFont(QFont("HelveticaNeueLT Pro 35 Th", 11))

        self.input_text = QLineEdit(self)
        self.input_text.setFont(QFont("HelveticaNeueLT Pro 35 Th", 11))
        self.input_text.setFocusPolicy(Qt.StrongFocus)
        self.input_text.textChanged.connect(self.input_text_modified)

        self.status_label = QLabel(self)
        self.status_label.setFont(QFont("Arial", 22))

        self.image_label = QLabel(self)
        self.image_label.setScaledContents(True)
        self.image_label.setAlignment(Qt.AlignCenter)

        self.description_label = QLabel(self)
        self.description_label.setFont(QFont("HelveticaNeueLT Pro 35 Th", 11))
        self.description_label.setWordWrap(True)
        self.description_label.setText('Details:\n-\n-\n-\n-\n-\n-\n-\n-\n')

        self.play_button = QtWidgets.QPushButton(self)
        self.play_button.setText(CAPTION_START)
        self.play_button.setFont(QFont("HelveticaNeueLT Pro 35 Th", 18))
        self.play_button.clicked.connect(self.play_button_clicked)
        self.play_button.setEnabled(False)

        # apply grid layout
        widget = QWidget()
        layout = QGridLayout()
        layout.addWidget(self.label, 0, 0, 1, 2)
        layout.addWidget(self.input_text, 1, 0, 1, 1)
        layout.addWidget(self.status_label, 1, 1, 1, 1)
        layout.addWidget(self.image_label, 2, 0, 1, 2)
        layout.addWidget(self.description_label, 3, 0, 1, 2)
        layout.addWidget(self.play_button, 4, 0, 1, 2)
        layout.setRowStretch(2, 9)
        layout.setRowStretch(3, 9)
        layout.setRowStretch(4, 3)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    @pyqtSlot()
    def pooling_fetched_data(self):
        '''
        A slot for processing the results of a fetched url.
        It invokes by emiting pooling signal
        '''
        valid = self.f_th.is_valid()
        if valid:
            self.change_label_icon(ICON_PASS)
            self.play_url = self.f_th.get_url()
            self.image_label.setPixmap(QPixmap(self.f_th.get_image()).scaled(self.image_label.size(), 
                                                                            Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            self.change_label_icon(ICON_FAIL)
            self.image_label.setPixmap(QPixmap())

        self.description_label_update(self.f_th.get_pafy())
        self.input_text.setEnabled(True)
        self.input_text.setFocus()
        self.play_button.setEnabled(valid)

    def description_label_update(self, pafy_):
        '''
        Updates the description label w/ pafy object attributes
        TBD
        '''
        text = ''
        if pafy_ is None:
            text = 'Details:\n-\n-\n-\n-\n-\n-\n-\n-\n'
        else:
            text = 'Details:\n' + 'Title: ' + pafy_.title +'\n-\n-\n-\n-\n-\n-\n-\n'
        self.description_label.setText(text)

    def input_text_modified(self, text):
        '''
        A slot for processing of changed text
        '''
        self.input_text.setEnabled(False)
        self.change_label_icon(ICON_SANDTIMER)
        self.f_th.fetch(text)

    def play_button_clicked(self):
        '''
        A slot for processing button clicks
        '''
        if self.play_button.text() == CAPTION_START:
            self.input_text.setEnabled(False)
            self.get_player().play()
            self.play_button.setText(CAPTION_STOP)
        elif self.play_button.text() == CAPTION_STOP:
            self.input_text.setEnabled(True)
            self.input_text.setFocus()
            self.input_text.selectAll()
            self.get_player().stop()
            self.destroy_player()
            self.play_button.setText(CAPTION_START)

    def change_label_icon(self, _color):
        '''
        Change icon depending on validity of youtube id
        '''
        if _color == ICON_SANDTIMER:
            self.status_label.setText('\u23F3')
            self.status_label.setStyleSheet('QLabel {color: #cccc00}')
        elif _color == ICON_PASS:
            self.status_label.setText('\u2713')
            self.status_label.setStyleSheet('QLabel {color: #009933}')
        elif _color == ICON_FAIL:
            self.status_label.setText('\u2718')
            self.status_label.setStyleSheet('QLabel {color: #cc2900}')

        self.status_label.adjustSize()

    def get_player(self):
        '''
        Gets player instance.
        If a player doesn't exist the new instance will be created.
        '''
        if self.player is None:
            self.player = vlc.MediaPlayer(self.play_url)
            
        return self.player

    def destroy_player(self):
        '''
        Destroy player
        '''
        self.player = None


def window():
    '''
    Main routine
    '''
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


# running
# url example: #
# https://youtu.be/2Lvdci4dQos
# https://www.youtube.com/watch?v=bGV1xYJFAEI
window()