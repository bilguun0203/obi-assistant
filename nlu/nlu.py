from rasa_nlu.model import Interpreter


def load_model(dir='model'):
    return Interpreter.load(dir)
