import json
from skills.currency import get_currency


def dispatch(intent):
    intent = json.loads(intent)
    result = ''
    if intent['intent']['confidence'] > 0.55:
        if intent['intent']['name'] == 'greeting':
            result = 'Сайн байна уу?'
        elif intent['intent']['name'] == 'get_time':
            time = ''
            result = 'Цаг ' + time + ' болж байна'
        elif intent['intent']['name'] == 'get_date':
            month = ''
            day = ''
            result = 'Өнөөдөр ' + month + ' сарын ' + day + ' өдөр'
        elif intent['intent']['name'] == 'get_day':
            day = ''
            result = 'Өнөөдөр ' + day + ' гараг'
        elif intent['intent']['name'] == 'get_currency':
            if len(intent['intent']['entities']) > 0:
                get_currency(intent['intent']['entities'][0]['value'])
            else:
                get_currency()
