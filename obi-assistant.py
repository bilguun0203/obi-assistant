import json
from nlu import nlu
from skills import skills
import utils.tts as tts


def request(str, obj):
    result = skills.dispatch(nlu_model.parse(s), obj)
    print(result['answer'])
    tts.play_wav(tts.get_wav(result['answer']))
    return result['obj']


if __name__ == "__main__":
    print('Loading Model...')
    nlu_model = nlu.load_model('nlu/model')
    print('Assistant ready')
    tmp = None
    while True:
        s = input('{} -> '.format(tmp))
        tmp = request(s, tmp)
