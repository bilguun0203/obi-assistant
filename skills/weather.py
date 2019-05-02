import requests
import json
import utils.config as conf

DAY_NAMES = [
    'өнөөдөр',
    'маргааш',
    'нөгөөдөр'
]

CONDITION_CODES = {
    '2xx': 'дуу цахилгаантай бороотой',
    '3xx': 'шиврээ бороотой',
    '5xx': 'бороотой',
    '6xx': 'цастай',
    '7xx': '',
    '800': 'цэлмэг',
    '801': 'багавтар үүлтэй',
    '802': '',
    '803': '',
    '804': 'үүлэрхэг'
}


WIND_DIRECTION = [
    'хойноос',
    'зүүн хойноос',
    'зүүнээс',
    'зүүн урдаас',
    'урдаас',
    'баруун урдаас',
    'баруунаас',
    'баруун хойноос',
]


def calc_wind_direction(degree=0):
    return round(degree/45) % 8


def get_weather(city='', day=None):
    loc_id = None
    result = ''
    city = city if city != '' else conf.config()['HOME_CITY']
    with open('./skills/city.list.json', 'r') as infile:
        cities = json.load(infile)
        for c in cities:
            if c['name_dative'].lower() == city.lower() or c['name'].lower() == city.lower():
                city = c['name_dative']
                loc_id = c['id']
                break
    if loc_id is None:
        return False
    if day in DAY_NAMES:
        js = api_call('forecast/daily', loc_id=loc_id)
        temp_high = 'хасах ' + str(round(js['list'][DAY_NAMES.index(day)]['temp']['max'])) if js['list'][DAY_NAMES.index(
            day)]['temp']['max'] < 0 else round(js['list'][DAY_NAMES.index(day)]['temp']['max'])
        temp_low = 'хасах ' + str(round(js['list'][DAY_NAMES.index(day)]['temp']['min'])) if js['list'][DAY_NAMES.index(
            day)]['temp']['min'] < 0 else round(js['list'][DAY_NAMES.index(day)]['temp']['min'])
        condition = 'цэлмэг'
        # return '{} {} {}, температур {} болон {} градусын хооронд байна'.format(city, day, condition, temp_low, temp_high)
        return '{} {} температур {} болон {} градусын хооронд байна'.format(city, day, temp_low, temp_high)
    else:
        js = api_call('weather', loc_id=loc_id)
        temp = 'хасах' + \
            str(round(js['main']['temp'])) if js['main']['temp'] < 0 else round(
                js['main']['temp'])
        wind_direction = ''
        wind_speed = 0
        if 'deg' in js['wind']:
            wind_direction = WIND_DIRECTION[calc_wind_direction(
                js['wind']['deg'])]
        if 'speed' in js['wind']:
            wind_speed = round(js['wind']['speed'])
        condition = 'цэлмэг'
        # return '{} одоо {}, {} градус, салхи {} {} метр секунд'.format(city, condition, temp, wind_direction, wind_speed)
        return '{} одоо {} градус, салхи {} {} метр секунд'.format(city, temp, wind_direction, wind_speed)


def api_call(wtype='weather', loc_id=2028461):
    url = 'https://api.openweathermap.org/data/2.5/{}?id={}&appid={}&units=metric&cnt=3'.format(
        wtype, loc_id, conf.config()['WEATHER_API_KEY'])
    return requests.get(url).json()
