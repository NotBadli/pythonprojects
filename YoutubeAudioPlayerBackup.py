import sys
import time

import pafy
import vlc
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QInputDialog, QLineEdit,
                             QMainWindow, QPushButton, QWidget)

font = QFont()
font.setFamily('Arial')
font.setPointSize(11)

infoFont = QFont()
infoFont.setFamily('Arial')
infoFont.setPointSize(13)

buttonFont = QFont()
buttonFont.setFamily('Arial')
buttonFont.setPointSize(20)

bigButtonFont = QFont()
bigButtonFont.setFamily('Arial')
bigButtonFont.setPointSize(23)

CAPTION_START = 'Start'
CAPTION_STOP = 'Stop'
CAPTION_RESUME = 'Resume'
CAPTION_PAUSE = 'Pause'

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.move(1495, 580)
        self.setFixedSize(850, 700)
        self.setWindowTitle('Youtube Audio Player')
        self.player = None
        
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('Paste youtube URL to play it in MP3 version!')
        self.label.move(25, 35)
        self.label.setFont(font)
        self.label.adjustSize()

        self.infoLabel = QtWidgets.QLabel(self)
        self.infoLabel.setText(' -')
        self.infoLabel.move(25, 190)
        self.infoLabel.setFont(infoFont)
        self.infoLabel.adjustSize()

        self.infoLabel1 = QtWidgets.QLabel(self)
        self.infoLabel1.setText(' -')
        self.infoLabel1.move(25, 270)
        self.infoLabel1.setFont(infoFont)
        self.infoLabel1.adjustSize()

        self.inputText = QLineEdit(self)
        self.inputText.setGeometry(25, 85, 800, 55)
        self.inputText.setFont(font)
        self.inputText.textChanged.connect(self.textModified)

        self.startB = QtWidgets.QPushButton(self)
        self.startB.setText(CAPTION_START)
        self.startB.clicked.connect(self.startClicked)
        self.startB.setGeometry(0, 352, 850, 348)
        self.startB.setFont(bigButtonFont)
        self.startB.setEnabled(False)

        self.pauseB = QtWidgets.QPushButton(self)
        self.pauseB.setText(CAPTION_PAUSE)
        self.pauseB.clicked.connect(self.pauseClicked)
        self.pauseB.setGeometry(0, 352, 850, 175)
        self.pauseB.setFont(buttonFont)
        self.pauseB.setHidden(True)

    def startClicked(self):
        v = pafy.new(self.inputText.text())
        try:
            if self.startB.text() == CAPTION_START:                                                                                                          
                self.getPlayer().play()
                self.infoLabel.setText(v.title)
                self.infoLabel.adjustSize()
                self.infoLabel1.setText(v.author)
                self.infoLabel1.adjustSize()
                self.inputText.setEnabled(False)
                self.startB.setText(CAPTION_STOP)
                self.startB.setFont(buttonFont)
                self.pauseB.setHidden(False)
                self.startB.setGeometry(0, 525, 850, 175)
            elif self.startB.text() == CAPTION_STOP:
                self.getPlayer().stop()
                self.inputText.setEnabled(True)
                self.inputText.setFocus()
                self.inputText.selectAll()
                self.player = None
                self.startB.setGeometry(0, 352, 850, 348)
                self.startB.setText(CAPTION_START)
                self.pauseB.setText(CAPTION_PAUSE)
                self.startB.setFont(bigButtonFont)
                self.pauseB.setHidden(True)
        except:
            self.startB.setEnabled(False)
            self.startB.setText('Video not found')

    def pauseClicked(self):
        if self.pauseB.text() == CAPTION_PAUSE:                                                                                                          
            self.getPlayer().pause()
            self.pauseB.setText(CAPTION_RESUME)
        elif self.pauseB.text() == CAPTION_RESUME:
            self.getPlayer().pause()
            self.pauseB.setText(CAPTION_PAUSE)

    def textModified(self):
        if self.inputText.text() == "":
            self.startB.setEnabled(False)
        else:
            self.startB.setText(CAPTION_START)
            self.startB.setEnabled(True)
    
    def playerWorker(self):
        url = self.inputText.text()                                                                                         
        video = pafy.new(url)                                                                                                                       
        best = video.getbestaudio()                                                                                                                 
        playurl = best.url                                                                                                                          
        player = vlc.MediaPlayer(playurl) 

        return player

    def getPlayer(self):
        if self.player is None:
            self.player = self.playerWorker()
        else:
            pass

        return self.player

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

# Example
# https://www.youtube.com/watch?v=eU32H6FpO2I&ab_channel=AmberGoldfire

window()
