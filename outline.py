# изменение регистра у элементов списка(букв)
# объект тот же самый
lstt = ['h', 'e', 'l', 'l', 'o']
print(f'lst before - {id(lstt)}')
lst_2 = lstt
for i in enumerate(lstt):
    lstt[i[0]] = i[1].upper()

print(lstt)
print(f'lst after - {id(lstt)}', '\n')

# создается новый объект
string = str(lst_2)
print(f'lst2 before - {id(lst_2)}')
print(string.upper())
print(f'lst2 after - {id(string.upper())}')