import json
from nlu import nlu
from skills import skills

if __name__ == "__main__":
    print('Loading Model...')
    nlu_model = nlu.load_model('nlu/model')
    print('Assistant ready')
    while True:
        s = input('-> ')
        print(skills.dispatch(nlu_model.parse(s)))
