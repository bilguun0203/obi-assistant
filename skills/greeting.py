import math
import random

GREETINGS = [
    'Сайн уу?',
    'Юу байна?',
    'Сайн байна уу?'
]


def greet(**kwargs):
    return GREETINGS[math.floor(random.random()*len(GREETINGS))]
