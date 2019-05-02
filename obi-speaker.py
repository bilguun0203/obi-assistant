#!/usr/bin/env python3
from precise_runner import PreciseEngine, PreciseRunner
import time
from pixel_ring import pixel_ring
import mraa
import os
import subprocess


# Pixel Ring initialization
en = mraa.Gpio(12)
if os.getuid() != 0:
    time.sleep(1)
en.dir(mraa.DIR_OUT)
en.write(0)
pixel_ring.set_brightness(20)


def on_activation():
    print('hello')
    pixel_ring.wakeup()
    subprocess.run(['aplay', 'dist/activate.wav'])
    time.sleep(3)
    pixel_ring.off()


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
