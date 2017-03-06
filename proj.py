from pygame import mixer
mixer.init()
mixer.music.load("b.wav")
mixer.music.play()
input()
for i in range(10):
    mixer.music.pause()
    input()
    mixer.music.unpause()
    input()

from pydub import AudioSegment
sound = AudioSegment.from_mp3("a.mp3")
sound.export("b.wav",format="wav") 
