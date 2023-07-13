import json
import pyaudio
from vosk import Model, KaldiRecognizer

model = Model('vosk-model-en-us-0.22-lgraph')
recognizer = KaldiRecognizer(model, 16000)
words = pyaudio.PyAudio()
stream = words.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()


def listening():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if (recognizer.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(recognizer.Result())
            if answer["text"]:
                yield answer["text"]


for text in listening():
    if "football" in text.lower():
        print(f"UkrBot: football is my favourite sport!")
        print(f"UkrBot: your text - {text}")
    else:
        print(f"User: {text}")