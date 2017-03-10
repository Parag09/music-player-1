import sys
from PyQt4 import QtGui ,QtCore
import os
from pygame import mixer
from threading import Thread
from pydub import AudioSegment
import pyaudio
import wave
global path
global path2
global t
global t2
isPlaying = False
started = False
recording = False
recordSlots = []  #[(s,e), (es), (), ()]
called = False

class Window(QtGui.QMainWindow):
    """docstring for ."""
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(200,200,500,500)
        self.setWindowTitle("PlayCord")
        self.firstWindow()
        self.setFixedSize(self.size())

        palette	= QtGui.QPalette()
        

        palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(QtGui.QPixmap("The Flatline.png")))

    
        self.setPalette(palette)

    def firstWindow(self):
        text = QtGui.QLabel(self)
        text.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        text.setText("OVERLAY TEXT")

        pic = QtGui.QLabel(self)
        pic.setGeometry(175, 175, 150, 150)
        #use full ABSOLUTE path to the image, not relative
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "\\paritosh.png"))
        pic.mousePressEvent = self.getOpenPath

        self.textBox = QtGui.QLineEdit(self)
        self.textBox.move(20, 100)
        self.textBox.resize(280,20)
##        self.browseButton = QtGui.QPushButton("Browse",self)
##        self.browseButton.clicked.connect(self.getOpenPath)
##        self.browseButton.resize(self.browseButton.sizeHint())
##        self.browseButton.move(400, 100)

        self.nextButton = QtGui.QPushButton("Next",self)
        self.nextButton.clicked.connect(self.secondWindow)
        self.nextButton.resize(self.nextButton.sizeHint())
        self.nextButton.move(100,400)
        self.show()

    def secondWindow(self):
        self.browseButton.hide()
        self.nextButton.hide()
        self.textBox.hide()
        self.playButton = QtGui.QPushButton("Play",self)
        self.playButton.clicked.connect(self.playPause)
        self.playButton.resize(self.playButton.sizeHint())
        self.playButton.move(0, 100)
        self.playButton.show()
        self.recordButton = QtGui.QPushButton("Start Recording", self)
        self.recordButton.clicked.connect(self.recordVar)
        self.recordButton.resize(self.recordButton.sizeHint())
        self.recordButton.move(0, 100)
        self.browseButton2 = QtGui.QPushButton("Browse",self)
        self.browseButton2.clicked.connect(self.getSavePath)
        self.browseButton2.resize(self.browseButton2.sizeHint())
        self.browseButton2.move(0, 100)
        self.nextButton2 = QtGui.QPushButton("Finish",self)
        self.nextButton2.clicked.connect(self.save)
        self.nextButton2.resize(self.nextButton.sizeHint())
        self.nextButton2.move(100, 100)

        self.nextButton3 = QtGui.QPushButton("complete",self)
        self.nextButton3.clicked.connect(self.complete)
        self.nextButton3.resize(self.nextButton.sizeHint())
        self.nextButton3.move(100, 100)

        self.nextButton3.show()

    def thirdWindow(self):
        self.playButton.hide()
        
        self.browseButton2.show()
        self.nextButton2.show()
        self.nextButton3.hide()

    def getOpenPath(self, event):
        global path

        path = QtGui.QFileDialog.getOpenFileName()
        self.textBox.setText(path)
            
    def getSavePath(self):
        global path2
        
        path2 = QtGui.QFileDialog.getSaveFileName()


    def save(self):
        song = AudioSegment.from_mp3(path)
        print("almost done")
        for i in range(len(recordSlots)):
            record = AudioSegment.from_wav(str(i+1)+".wav")
            song = song[:recordSlots[i]] + record + song[recordSlots[i]:]
        song.export(path2, format = "mp3")
        print("done")
        sys.exit()
        
    def playPause(self):
        global started
        global isPlaying
        global recordSlots
        global t2
        if not started :
            mixer.init()
            mixer.music.load(path)
            mixer.music.play()
            started = True
            isPlaying= True
            t2 = Thread(target = self.isFinished)
            t2.start()
            self.playButton.setText("Pause")
        elif isPlaying:
             mixer.music.pause()
             recordSlots += [mixer.music.get_pos()]
             self.playButton.hide()
             self.recordButton.show()
             isPlaying = False
             self.playButton.setText("Play")
        else:
            mixer.music.unpause()
            isPlaying= True
            self.playButton.setText("Pause")
    def recordVar(self):
        global recording
        global t
        if not recording:
            recording = True
            t = Thread(target = self.record)
            t.start()
            self.recordButton.setText("Stop Recording")
        else:
            self.recordButton.setText("Start Recording")
            self.playButton.setText("Play")
            recording = False
            self.recordButton.hide()
            self.playButton.show()

    def record(self):
        global recording
        p=pyaudio.PyAudio()
        FRAMES_PERBUFF = 2048 #   no of FRAMES_PERBUFFER
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        FRAME_RATE = 44100
        stream = p.open(format = FORMAT, channels = CHANNELS, rate = FRAME_RATE, input = True, frames_per_buffer = FRAMES_PERBUFF)
        frames = []
        while recording:
            data = stream.read(FRAMES_PERBUFF)
            frames.append(data) # 2 bytes(16 bits) per channel
        stream.stop_stream()
        stream.close()
        p.terminate()
        wf = wave.open(str(len(recordSlots))+'.wav', 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(FRAME_RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    def isFinished(self):
        global t2
        while mixer.music.get_pos() != -1:
            pass
        called = True
        self.thirdWindow()

    def complete(self):
        mixer.music.pause()
        self.thirdWindow()

app=QtGui.QApplication(sys.argv)
w=Window()
sys.exit(app.exec_())
