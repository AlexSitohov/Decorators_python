try:
    def decorator_func(func):
        def wrapper(a, b):
            return func(a, b)

        return wrapper


    @decorator_func
    def div(a, b):
        return f'{a} / {b} = {a / b}, int({int(a / b)})'


    first_value = div

    print(first_value(int(input('enter a ')), int(input('enter b '))))
except Exception as ex:
    print(ex)
finally:
    print('end work of function')
