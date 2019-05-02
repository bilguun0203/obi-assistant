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


# Pixel Ring initialization
en = mraa.Gpio(12)
if os.getuid() != 0:
    time.sleep(1)
en.dir(mraa.DIR_OUT)
en.write(0)
pixel_ring.set_brightness(20)

assistant = Assistant('nlu/model', pixel_ring, True)


def stt():
    audio_file = '.tmp/stt.flac'
    text = False
    subprocess.run(['rec', '-c', '1', '-r', '16000', '-d', audio_file,
                    'trim', '0', '15', 'silence', '1', '0.1', '0.3%', '1', '3.0', '0.3%'])
    output = str(subprocess.check_output(
        "curl -T {} {}".format(audio_file, conf.config()['STT_URL']), shell=True), 'utf-8')
    print(output)
    if output == 'No workers available':
        return False
    response = json.loads(output)
    print(response)
    if response['status'] == 0:
        text = response['hypotheses'][0]['utterance']
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
    main()
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            break
    pixel_ring.off()
    time.sleep(1)

en.write(1)
