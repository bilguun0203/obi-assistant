import json
from nlu import nlu
from skills import skills
import utils.tts as tts


def request(str):
    result = skills.dispatch(nlu_model.parse(s))
    print(result)
    tts.play_wav(tts.get_wav(result))


if __name__ == "__main__":
    print('Loading Model...')
    nlu_model = nlu.load_model('nlu/model')
    print('Assistant ready')
    while True:
        s = input('-> ')
        request(s)
