import pyaudio
import wave
import numpy as np

CHUNK = 1024

wf = wave.open('e.wav', 'rb')

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)


data = wf.readframes(CHUNK)
# stream.write(0.5*data.astype(np.int16))
# stream.stop_stream()
# stream.close()
# p.terminate()
while data != b'':
    stream.write(data)
    data = wf.readframes(CHUNK)
    print(data)
print(1111)
stream.stop_stream()
stream.close()

p.terminate()

