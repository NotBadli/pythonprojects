import sys

import pafy, time
import vlc
import zope.event
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QInputDialog, QLineEdit,
                             QMainWindow, QWidget)


CAPTION_START = 'Start'
CAPTION_STOP = 'Stop'
ICON_SANDTIMER = 'yellow'
ICON_PASS = 'green'
ICON_FAIL = 'red'

player = None
playurl = ''

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowFlag(Qt.WindowMaximizeButtonHint)
        self.move(1495, 580)
        self.setFixedSize(850, 1000)
        self.setWindowTitle('Youtube Audio Player')
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('Paste youtube URL to play it in MP3 version!')
        self.label.move(25, 50)
        self.label.setFont(QFont("Arial", 11))
        self.label.adjustSize()

        self.InputText = QLineEdit(self)
        self.InputText.setGeometry(25, 100, 725, 55)
        self.InputText.setFont(QFont("Arial", 11))
        self.InputText.textChanged.connect(self.InputTextModified)
        zope.event.subscribers.append(self.setTextChangedNotification)

        self.StatusLabel = QtWidgets.QLabel(self)
        self.StatusLabel.setFont(QFont("Arial", 22))
        self.StatusLabel.move(750, 90)
        self.changeLabelIcon(ICON_FAIL)

        self.StartB = QtWidgets.QPushButton(self)
        self.StartB.setText(CAPTION_START)
        self.StartB.setGeometry(0, 825, 850, 175)
        self.StartB.setFont(QFont("Arial", 18))
        self.StartB.clicked.connect(self.StartClicked)
        self.StartB.setEnabled(False)

    def setTextChangedNotification(self, text):
        self.changeLabelIcon(ICON_SANDTIMER)
        # time.sleep(5)
        valid = self.isValid(text)
        if valid:
            self.changeLabelIcon(ICON_PASS)
        else:
            self.changeLabelIcon(ICON_FAIL)
            
        self.StartB.setEnabled(valid)
    
    def InputTextModified(self, text):
        zope.event.notify(text)
                
    def changeLabelIcon(self,_color):
        if _color == ICON_SANDTIMER:
            self.StatusLabel.setText('\u23F3')
            self.StatusLabel.setStyleSheet('QLabel {color: #cccc00}')
        elif _color == ICON_PASS:
            self.StatusLabel.setText('\u2713')
            self.StatusLabel.setStyleSheet('QLabel {color: #009933}')
        elif _color == ICON_FAIL:
            self.StatusLabel.setText('\u2718')
            self.StatusLabel.setStyleSheet('QLabel {color: #cc2900}')
        
        self.StatusLabel.adjustSize()

    def StartClicked(self):
        if self.StartB.text() == CAPTION_START:
            self.InputText.setEnabled(False)
            self.getPlayer().play()
            self.StartB.setText(CAPTION_STOP)
        elif self.StartB.text() == CAPTION_STOP:
            self.InputText.setEnabled(True)
            self.getPlayer().stop()
            self.destroyPlayer()
            self.StartB.setText(CAPTION_START)

    def getPlayer(self):
        global player
        if player == None:                                                                                                                   
            player = vlc.MediaPlayer(playurl)
        
        return player

    def destroyPlayer(self):
        global player
        player = None

    def isValid(self, text):
        valid = False
        try:
            video = pafy.new(text)                                                                                                                       
            best = video.getbestaudio()                                                                                                                 
            global playurl
            playurl = best.url
            valid = True   
        except:
            pass

        return valid


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
