import speech_recognition as sr
import sys

try:
    audio_file = sys.argv[1]
except:
    print('Missing audio file')

r = sr.Recognizer()

with sr.AudioFile(audio_file) as source:
    audio = r.listen(source)

text = r.recognize_google(audio)
print(text)
