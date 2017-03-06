from pygame import mixer
mixer.init()
mixer.music.load("a.mp3")
mixer.music.play()
input()
for i in range(10):
    mixer.music.pause()
    print(mixer.music.get_pos())
    input()
    mixer.music.unpause()
    input()

from pydub import AudioSegment
sound = AudioSegment.from_mp3("a.mp3")
sound.export("b.wav",format="wav") 
