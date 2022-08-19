def ingredients(func):
    def wrapper():
        print("#помидоры#")
        func()
        print("~салат~")

    return wrapper


def bread(func):
    def wrapper():
        func()
        print("<\______/>")

    return wrapper


@bread
@ingredients
def sandwich():
    print("--ветчина--")


sandwich()
