from datetime import datetime
from operator import index
from time import sleep


def decorator_func(func):
    def wrapper():
        time_start = datetime.now()
        func()
        sleep(3)
        print(f'Время выполнения функции {some_func.__name__} - {datetime.now() - time_start}')

    return wrapper


@decorator_func
def some_func():
    print('произвольная функция')


some_func()
