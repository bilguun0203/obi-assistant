from datetime import date, datetime


WEEKDAY_NAMES = [
    'Даваа',
    'Мягмар',
    'Лхагва',
    'Пүрэв',
    'Баасан',
    'Бямба',
    'Ням',
]


def get_time():
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    return str(hour) + ' цаг ' + str(minute) + ' минут болж байна'


def get_day():
    today = date.today()
    day = WEEKDAY_NAMES[today.weekday()]
    return 'Өнөөдөр ' + day + ' гараг'


def get_date():
    today = date.today()
    month = today.month
    day = today.day
    return 'Өнөөдөр ' + str(month) + ' сарын ' + str(day) + '-ны өдөр'
