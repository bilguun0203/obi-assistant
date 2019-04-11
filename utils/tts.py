import requests
import pyaudio
import wave
from utils.config import config


def get_wav(sentence=''):
    url = config()['TTS_URL'] + \
        str(sentence)
    r = requests.get(url)
    with open('.tmp/tts.wav', 'wb') as f:
        f.write(r.content)
    return './.tmp/tts.wav'


def play_wav(location='.tmp/tts.wav'):
    chunk = 1024

    f = wave.open(location, "rb")
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                    channels=f.getnchannels(),
                    rate=f.getframerate(),
                    output=True)
    data = f.readframes(chunk)
    while data:
        stream.write(data)
        data = f.readframes(chunk)

    stream.stop_stream()
    stream.close()

    p.terminate()
