import requests
import math


CURRENCIES = {
    'доллар': 'USD',
    'евро': 'EUR',
    'иен': 'JPY',
    'франк': 'CHF',
    'крон': 'SEK',
    'фунт': 'GBP',
    'лев': 'BGN',
    'унгарын форинт': 'HUF',
    'рупи': 'INR',
    'хонгконг доллар': 'HKD',
    'египетийн фунт': 'EGP',
    'рубль': 'RUB',
    'тэнгэ': 'KZT',
    'юань': 'CNY',
    'вон': 'KRW',
    'канад доллар': 'CAD',
    'австрали доллар': 'AUD',
    'чех крон': 'CZK',
    'тайвань доллар': 'TWD',
    'тайланд бат': 'THB',
    'индонези рупи': 'IDR',
    'ринггит': 'MYR',
    'сингапур доллар': 'SGD',
    'дирхам': 'AED',
    'кувейт динар': 'KWD',
    'шинэ зеланд доллар': 'NZD',
    'данийн крон': 'DKK',
    'польшийн злот': 'PLN',
    'украйны гривн': 'UAH',
    'норвегийн крон': 'NOK',
    'непалийн рупи': 'NPR',
    'өмнөд африкийн ранд': 'ZAR',
    'туркийн лира': 'TRY',
    'вьетнам донг': 'VND'
}


def get_currency(currency='Доллар'):
    url = 'https://monxansh.appspot.com/xansh.json?currency='
    r = requests.get(url=url + CURRENCIES[currency.lower()])
    price = math.floor(r.json()[0]['rate_float'])
    return currency + ' ' + str(price) + ' төгрөг байна'
