import sys
from PyQt4 import QtGui ,QtCore
from pygame import mixer
from threading import Thread
from pydub import AudioSegment
import pyaudio
import wave
global path
global t
isPlaying = False
started = False
recording = False
recordSlots = []  #[(s,e), (es), (), ()]

class Window(QtGui.QMainWindow):
    """docstring for ."""
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(200,200,500,500)
        self.setWindowTitle("PlayCord")
        self.firstWindow()

    def firstWindow(self):
        self.browseButton = QtGui.QPushButton("Browse",self)
        self.browseButton.clicked.connect(self.getOpenPath)
        self.browseButton.resize(self.browseButton.sizeHint())
        self.browseButton.move(0, 100)

        self.nextButton = QtGui.QPushButton("Next",self)
        self.nextButton.clicked.connect(self.secondWindow)
        self.nextButton.resize(self.nextButton.sizeHint())
        self.nextButton.move(100, 100)
        self.show()

    def secondWindow(self):
        self.browseButton.hide()
        self.nextButton.hide()
        self.playButton = QtGui.QPushButton("Play",self)
        self.playButton.clicked.connect(self.playPause)
        self.playButton.resize(self.playButton.sizeHint())
        self.playButton.move(0, 100)
        self.playButton.show()
        self.recordButton = QtGui.QPushButton("Record", self)
        self.recordButton.clicked.connect(self.recordVar)
        self.recordButton.resize(self.recordButton.sizeHint())
        self.recordButton.move(0, 100)

    def thirdWindow(self):
        self.playButton.hide()
        self.recordButton.hide()
        self.browseButton = QtGui.QPushButton("Browse",self)
        self.browseButton.clicked.connect(self.getSavePath)
        self.browseButton.resize(self.browseButton.sizeHint())
        self.browseButton.move(0, 100)
        self.browseButton.show()

    def getOpenPath(self):
        global path
        path = QtGui.QFileDialog.getOpenFileName()

    def getSavePath(self):
        global path
        path = QtGui.QFileDialog.getSaveFileName()
        song = AudioSegment.from_mp3(path)
        for i in range(len(recordSlots)):
            record = AudioSegment.from_wav(str(i+1)+".wav")
            song = song[:recordSlots[i]] + record + song[recordSlots[i]:]
        song.export(path, format = "mp3")
    def playPause(self):
        global started
        global isPlaying
        global recordSlots
        if not started :
            mixer.init()
            mixer.music.load(path)
            mixer.music.play()
            started = True
            isPlaying= True
            t2 = Thread(target = self.isFinished)
            t2.start()
        elif isPlaying:
             mixer.music.pause()
             recordSlots += [mixer.music.get_pos()]
             self.playButton.hide()
             self.recordButton.show()
             isPlaying = False
        else:
            mixer.music.unpause()
            isPlaying= True
    def recordVar(self):
        global recording
        if not recording:
            recording = True
            t = Thread(target = self.record)
            t.start()
        else:
            #t.join()
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
        l = len(AudioSegment.from_mp3(path))
        while mixer.music.get_pos() != l:
            pass
        self.thirdWindow()
app=QtGui.QApplication(sys.argv)
w=Window()
sys.exit(app.exec_())