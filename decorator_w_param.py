# Decorator w parameters
def outer_2(*bargs, **bkwargs):
    def outer(func):
        def wrapper(*args, **kwargs):
            print(*bargs, **bkwargs)
            return func(*args, **kwargs)

        return wrapper

    return outer


# No logic just decorator w param for test
@outer_2('Some', 'Text', 1, 2, 3, 4, 5, 6, 7, 8, 9, [*range(1, 6)])
def div(a, *args):
    some_lst = []
    for i in args:
        some_lst.append(i ** a)
    return some_lst


print(div(2, *range(1, 11)))
