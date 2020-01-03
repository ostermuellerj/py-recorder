# ~ https://github.com/jiaaro/pydub
# ~ https://stackoverflow.com/questions/4039158/mixing-two-audio-files-together-with-python/53978531

from pydub import AudioSegment
from pydub.playback import play

# ~ sound1 = AudioSegment.from_file("/path/to/my_sound.wav")
# ~ sound2 = AudioSegment.from_file("/path/to/another_sound.wav")
sound1 = AudioSegment.from_file("a.m4a")
sound2 = AudioSegment.from_file("b.m4a")

combined = sound1.overlay(sound2)

combined.export("combined.mp4", format='mp4')

sound = AudioSegment.from_file("combined.mp4", format="mp4")
play(sound)
