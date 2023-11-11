# 5. Дорабатываем задачу 4. Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить.
# В этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.


import datetime
import argparse
import logging

FORMAT = '{levelname}, {asctime}, {msg}'
logging.basicConfig(format=FORMAT, style='{', filename='logs.log', filemode='w+', encoding='utf-8', level=logging.ERROR)

logger = logging.getLogger(__name__)


def log_dec(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f'Error {e} in the function {func.__name__} arguments {args}, {kwargs}')
            return None

    return wrapper


MONTHS = {'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня': 6, 'июля': 7, 'августа': 8,
          'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12}
MONTHSREV = dict(map(lambda x: (x[1], x[0]), MONTHS.items()))

WEEKDAYS = {'понедельник': 1, 'вторник': 2, 'среда': 3, 'четверг': 4, 'пятница': 5, 'суббота': 6, 'воскресенье': 7}
WEEKDAYSREV = dict(map(lambda x: (x[1], x[0]), WEEKDAYS.items()))


@log_dec
def par():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', default=1)
    parser.add_argument('-w', '--weekday', default=WEEKDAYSREV.get(datetime.datetime.now().weekday, 'понедельник'))
    parser.add_argument('-m', '--month', default=MONTHSREV.get(datetime.datetime.now().month, 'января'))
    args = parser.parse_args()
    return print_date(f'{args.number}-й {args.weekday} {args.month}')


@log_dec
def print_date(str_day):
    num, weekday, month = str_day.split()
    num = int(num[0])
    weekday = WEEKDAYS[weekday] - 1
    month = MONTHS[month]

    count = 0
    for i in range(1, 32):
        temp_date = datetime.datetime(datetime.datetime.now().year, month, i)
        if temp_date.weekday() == weekday:
            count += 1
            if count == num:
                return temp_date
            raise ValueError


print(par())
