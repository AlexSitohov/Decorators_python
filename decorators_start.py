def decorator_func(func):
    def wrapper():
        print('начало')
        func()
        print('конец')

    return wrapper


@decorator_func
def some_func():
    print('произвольная функция')


some_func()
