import pyaudio
p=pyaudio.PyAudio()
FRAMES_PERBUFF = 2048 #   no of FRAMES_PERBUFFER
FORMAT = pyaudio.paInt16
CHANNELS = 1
FRAME_RATE = 44100
stream = p.open(format = FORMAT, channels = CHANNELS, rate = FRAME_RATE, input = True, frames_per_buffer = FRAMES_PERBUFF)
frames = []
print("start")

RECORD_SECONDS = 5
nchunks = int(RECORD_SECONDS * FRAME_RATE / FRAMES_PERBUFF)
for i in range(0, nchunks):
    data = stream.read(FRAMES_PERBUFF)
    frames.append(data) # 2 bytes(16 bits) per channel
print("* done recording")
stream.stop_stream()
stream.close()
p.terminate()

print ("done")
import wave
import random
x =random.randint(1,1000000)
wf = wave.open(str(x)+'.wav', 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(FRAME_RATE)
wf.writeframes(b''.join(frames))
wf.close()
