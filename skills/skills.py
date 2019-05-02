import json
import math
import random
import skills.greeting as greeting
import skills.currency as currency
import skills.time_n_date as time_n_date
import skills.weather as weather
import skills.order as order

DO_NOT_KNOW = [
    'Таны юу яриад байгааг ойлгохгүй байна',
    'Миний чадахаар зүйл биш байна',
    'Ойлгосонгүй',
    'Асуултаа шалгаад дахин асууна уу',
    'Дахиад хэлнэ үү'
]


def dispatch(intent, obj=None):
    result = {'obj': None, 'answer': ''}
    if intent['intent']['confidence'] > 0.5:
        if intent['intent']['name'] == 'greeting':
            result['answer'] = greeting.greet()
        elif intent['intent']['name'] == 'get_time':
            result['answer'] = time_n_date.get_time()
        elif intent['intent']['name'] == 'get_date':
            result['answer'] = time_n_date.get_date()
        elif intent['intent']['name'] == 'get_day':
            result['answer'] = time_n_date.get_day()
        elif intent['intent']['name'] == 'get_weather':
            p = {}
            for entity in intent['entities']:
                p[entity['entity']] = entity['value']
            result['answer'] = weather.get_weather(**p)
        elif intent['intent']['name'] == 'get_currency':
            if len(intent['entities']) > 0:
                result['answer'] = currency.get_currency(
                    intent['entities'][0]['value'])
            else:
                result['answer'] = currency.get_currency()
        elif intent['intent']['name'] == 'order':
            if len(intent['entities']) > 0:
                result['obj'] = order.Order(intent['entities'][0]['value'])
            else:
                result['obj'] = order.Order()
            result['answer'] = 'ямар хэмжээтэй {} захиалах вэ'.format(
                result['obj']._name)
        elif intent['intent']['name'] == 'order_size':
            if len(intent['entities']) > 0:
                result['obj'] = obj.set_size(intent['entities'][0]['value'])
            else:
                result['obj'] = obj.set_size()
            result['answer'] = 'хэдэн ширхэгийг захиалах вэ'
        elif intent['intent']['name'] == 'order_quantity':
            if len(intent['entities']) > 0:
                obj.set_quantity(int(intent['entities'][0]['value']))
            else:
                obj.set_quantity()
            result['answer'] = obj.order()
    else:
        result = False
    if result == False:
        result = {'answer': DO_NOT_KNOW[math.floor(
            random.random() * len(DO_NOT_KNOW))], 'obj': obj}
    return result
