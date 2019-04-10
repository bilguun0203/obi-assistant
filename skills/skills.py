import json
import math
import random
import skills.greeting as greeting
import skills.currency as currency
import skills.time_n_date as time_n_date

DO_NOT_KNOW = [
    'Таны юу яриад байгааг ойлгохгүй байна',
    'Миний чадахаар зүйл биш байна',
    'Ойлгосонгүй',
    'Асуултаа шалгаад дахин асууна уу'
]


def dispatch(intent):
    result = ''
    print(intent['intent'])
    if intent['intent']['confidence'] > 0.55:
        if intent['intent']['name'] == 'greeting':
            result = greeting.greet()
        elif intent['intent']['name'] == 'get_time':
            result = time_n_date.get_time()
        elif intent['intent']['name'] == 'get_date':
            result = time_n_date.get_date()
        elif intent['intent']['name'] == 'get_day':
            return time_n_date.get_day()
        elif intent['intent']['name'] == 'get_currency':
            if len(intent['entities']) > 0:
                result = currency.get_currency()(
                    intent['entities'][0]['value'])
            else:
                result = currency.get_currency()()
    else:
        result = DO_NOT_KNOW[math.floor(random.random()*len(DO_NOT_KNOW))]
    return result
