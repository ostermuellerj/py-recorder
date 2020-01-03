from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_file("beepstop.wav", format="wav")
play(sound)
