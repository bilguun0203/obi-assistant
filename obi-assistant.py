import json
from nlu import nlu
from skills import skills
import utils.tts as tts
import subprocess


def load_model(path='nlu/model'):
    print('Loading Model...')
    model = nlu.load_model('nlu/model')
    return model


def request(str, obj):
    result = skills.dispatch(nlu_model.parse(s), obj)
    print(result['answer'])
    subprocess.run(['aplay', tts.get_wav(result['answer'])])
    return result['obj']


if __name__ == "__main__":
    nlu_model = load_model('nlu/model')
    print('Assistant ready')
    tmp = None
    while True:
        s = input('{} -> '.format(tmp))
        tmp = request(s, tmp)
