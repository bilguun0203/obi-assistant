import json
from nlu import nlu
from utils.response import Response


def load_model(path='nlu/model'):
    print('Loading Model...')
    model = nlu.load_model('nlu/model')
    return model


class Assistant:
    def __init__(self, model_path='nlu/model'):
        self.nlu_model = load_model(model_path)
        self.respond = Response(None, False)

    def request(self, str, obj):
        result = self.respond.think(self.nlu_model.parse(str), obj)
        print(result['answer'])
        self.respond.speak(result['answer'])
        self.respond.reset()
        return result['obj']


if __name__ == "__main__":
    assistant = Assistant('nlu/model')
    print('Assistant ready')
    assistant.respond.wakeup()
    tmp = None
    while True:
        s = input('{} -> '.format(tmp))
        tmp = assistant.request(s, tmp)
