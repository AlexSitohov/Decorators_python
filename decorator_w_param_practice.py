def outer_2(N):  # Параметры декоратора outer_2
    def outer(func):  # Функция div
        def wrapper(*args, **kwargs):  # Параметры функции div
            for itr in range(1, N + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as ex:
                    print(f'{itr} - {ex}')

        return wrapper

    return outer


@outer_2(N=100)
def div(*args):
    some_lst = []
    for i in args:
        some_lst.append(i ** 2)
    return some_lst


print(div(1, 2, 3, 4, 'a'))
