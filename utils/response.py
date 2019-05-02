import subprocess
import utils.tts as tts
from skills import skills


class Response:
    def __init__(self, pixel_ring, speaker=False):
        self.pixel_ring = pixel_ring
        self.speaker = speaker

    def wakeup(self):
        print('Wakeup')
        if self.speaker:
            self.pixel_ring.wakeup()
        # subprocess.run(['aplay', '-r', '44100', '-q', 'dist/activate.wav'])
        subprocess.run(['play', 'dist/activate.wav'])

    def think(self, intent, obj):
        print('Thinking...')
        if self.speaker:
            self.pixel_ring.think()
        return skills.dispatch(intent, obj)

    def speak(self, response):
        print('Speaking...')
        if self.speaker:
            self.pixel_ring.speak()
        # subprocess.run(['aplay', '-r', '16000', '-q', tts.get_wav(response)])
        subprocess.run(['play', tts.get_wav(response)])

    def reset(self):
        print('Reset')
        if self.speaker:
            self.pixel_ring.off()
