import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile('audio_file.wav') as source:
    audio_text = r.record(source)
    text = r.recognize_google(audio_text)
    print(text)
