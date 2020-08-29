import speech_recognition as sr
import sys

# audio filepath
try:
    audio_file = sys.argv[1]
except:
    print('Missing audio file')

# transcription filepath (optional)
text_file = ''
try:
    text_file = sys.argv[2]
except:
    pass

# transcribe audio to text
r = sr.Recognizer()

with sr.AudioFile(audio_file) as source:
    audio = r.listen(source)

text = r.recognize_google(audio)

# save transcription (if applicable)
if text_file:
    text_file = open(text_file, 'w')
    text_file.write(text)

# print transcription
print(text)
