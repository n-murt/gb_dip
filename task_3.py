# 3. Доработаем задачу 2. Сохраняйте в лог файл раздельно: уровень логирования,
# дату события, имя функции (не декоратора), аргументы вызова, результат
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


@log_dec
def my_func(storage, key, value=None):
    return storage[key]


@log_dec
def my_func_div(divisor, dividend):
    return dividend / divisor


f = {'f': '1', 'd': '3', 's': '5'}

print(my_func(f, 'b', 2))
print(my_func_div(0, 100))
