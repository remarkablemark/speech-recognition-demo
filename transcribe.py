import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile('audio.wav') as source:
    audio = r.listen(source)

text = r.recognize_google(audio)
print(text)
