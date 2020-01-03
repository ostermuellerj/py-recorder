import sounddevice as sd
import sys
from scipy.io.wavfile import write

# ~ print(sys.argv[0])
# ~ print(sys.argv)

takeLength = sys.argv[1]
sampleRate = sys.argv[2]
# ~ noiseType = sys.argv[3]

fs = 44100  # Sample rate
seconds = 3  # Duration of recording

# ~ myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
myrecording = sd.rec(int(float(takeLength) * float(sampleRate)), samplerate=float(sampleRate), channels=2)
sd.wait()  # Wait until recording is finished
write('output.wav', fs, myrecording)  # Save as WAV file 
