from random import choice
#
# # изменение регистра у элементов списка(букв)
# # объект тот же самый
# lstt = ['h', 'e', 'l', 'l', 'o']
# print(f'lst before - {id(lstt)}')
# lst_2 = lstt
# # for i in enumerate(lstt):
# #     lstt[i[0]] = i[1].upper()
# for i in lstt:
#     lstt[lstt.index(i)] = i.upper()
#
# print(lstt)
# print(f'lst after - {id(lstt)}', '\n')
#
# # создается новый объект
# string = str(lst_2)
# print(f'lst2 before - {id(lst_2)}')
# print(string.upper())
# print(f'lst2 after - {id(string.upper())}')
#
# from collections import Counter
#
# lst = [1, 4, 4, 4, 2, 5, 6, 6, 7, 8, 9, 10]
# frequent = max(set(lst), key=lst.count)
# print(frequent, lst.count(frequent))
# print(Counter(lst))
#
# k = 'abc'
# i = iter(k)
# next(i)
# print(next(i))


# Бинарный поиск символа в неупорядоченной строке
def decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Цель еще не найдена...')
        return func(*args, **kwargs)

    return wrapper


@decorator
def poisk(some_str, some_str_2, target, iteraciya):
    symbol = choice(some_str)
    print(f'Итерация - {iteraciya} выберем наугад символ - {symbol}  из строки {some_str} длинной {len(some_str)}',
          '\n')
    if symbol == target:
        c = 1
        return f'Цель найдена за {iteraciya} итераций. Индекс цели в строке - {some_str_2.index(symbol)}'
    else:
        c = 1
        sl = some_str[:int((len(some_str) / 2))]
        sp = some_str[int((len(some_str) / 2)):]
        if target in sl:
            c = 1

            return poisk(sl, some_str_2, target, iteraciya + 1)
        if target in sp:
            c = 1

            return poisk(sp, some_str_2, target, iteraciya + 1)


some_str = 'abcнdebcfdeolkjh'
some_str_2 = some_str
print(poisk(some_str, some_str_2, target='f', iteraciya=1))
