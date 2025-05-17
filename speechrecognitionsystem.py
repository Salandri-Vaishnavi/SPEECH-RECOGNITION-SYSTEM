import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
import tempfile

# Parameters
duration = 4 # seconds
fs = 44100  # sample rate

# Record audio using sounddevice
print("Recording for {} seconds...".format(duration))
recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
sd.wait()
print("Recording complete.")

# Save the recording temporarily as a WAV file
with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
    wav.write(f.name, fs, recording)
    wav_filename = f.name

# Recognize the speech using the Google Web Speech API
recognizer = sr.Recognizer()
with sr.AudioFile(wav_filename) as source:
    audio_data = recognizer.record(source)

try:
    print("Recognizing...")
    text = recognizer.recognize_google(audio_data)
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, could not understand the audio.")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
