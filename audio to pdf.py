import speech_recognition as sr

# Create a recognizer object
r = sr.Recognizer()

# Load the audio file
with sr.AudioFile('machine.wav') as source:
    audio = r.record(source)

# Perform recognition
text = r.recognize_sphinx(audio)
print(text)

