from pydub import AudioSegment
import pyaudio
song = AudioSegment.from_mp3("a.mp3")
record = AudioSegment.from_wav("recorded_audio.wav")
merge = song[:10000]+record + song[:10000]
merge.export("mashup.mp3", format="mp3"
