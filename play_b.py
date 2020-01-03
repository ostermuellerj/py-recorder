from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_file("b.m4a", format="m4a")
play(sound)
