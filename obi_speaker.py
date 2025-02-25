#!/usr/bin/env python3
from precise_runner import PreciseEngine, PreciseRunner
import time
from pixel_ring import pixel_ring
import mraa
import os
import json
import subprocess
from utils.response import Response
from obi_assistant import Assistant
import utils.config as conf
import pyaudio
import wave
import argparse


SOX = False

# Pixel Ring initialization
en = mraa.Gpio(12)
if os.getuid() != 0:
    time.sleep(1)
en.dir(mraa.DIR_OUT)
en.write(0)
pixel_ring.set_brightness(20)

pixel_ring.wakeup()

assistant = Assistant('nlu/model', pixel_ring, True)


def record(file_name='.tmp/stt.wav', duration=5):
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    CHUNK = 1024
    RECORD_SECONDS = duration
    WAVE_OUTPUT_FILENAME = file_name

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("recording...")
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("finished recording")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()


def stt():
    audio_file = '.tmp/stt.flac'
    text = False
    if SOX:
        subprocess.call(['rec', '-c', '1', '-r', '16000', '-d', audio_file,
                         'trim', '0', '15', 'silence', '1', '0.1', '0.3%', '1', '3.0', '0.3%'])
    else:
        record(audio_file)
    output = str(subprocess.check_output(
        "curl -T {} {}".format(audio_file, conf.config()['STT_URL']), shell=True), 'utf-8')
    print(output)
    if output == 'No workers available':
        return False
    response = json.loads(output)
    print(response)
    if response['status'] == 0:
        text = response['hypotheses'][0]['utterance']
        print('>>', text)
    return text


def on_activation():
    tmp = None
    loop = True
    while loop:
        assistant.respond.wakeup()
        result = stt()
        if result != False and type(result) is str:
            tmp = assistant.request(result)
            loop = tmp is not None
        else:
            loop = False
        assistant.respond.reset()


def main():
    # Wake word listener initialization
    engine = PreciseEngine(
        'dist/precise-engine/precise-engine', 'dist/hey-obi/hey-obi.pb')
    runner = PreciseRunner(engine, on_activation=on_activation)

    runner.start()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OBI SPEAKER')
    parser.add_argument('--sox', action='store_true')
    args = parser.parse_args()
    SOX = args.sox
    main()
    pixel_ring.off()
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            break
    pixel_ring.off()
    time.sleep(1)

en.write(1)
