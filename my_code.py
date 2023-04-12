import speech_recognition as sr
from pydub import AudioSegment

r = sr.Recognizer()

sound = AudioSegment.from_mp3("Sharmishtha.mp3")
sound.export("Sharmishtha.wav", format="wav")

with sr.AudioFile('Sharmishtha.wav') as source:
    audio_text = r.record(source)
    text = r.recognize_google(audio_text)
    print(text)
