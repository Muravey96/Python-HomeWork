# кол-во значений во множестве 

size_n = int(input('Введите размер 1го списка: '))

# Заполняем первое множество
chars_n = set(input() for _ in range(size_n))

size_m = int(input('Введите размер 2го списка: '))
chars_m = set(input() for _ in range(size_m))

print(chars_n)
print(chars_m)

# объединенное множество с пересекающимися значениями. 

print(sorted(chars_n.intersection(chars_m)))

""" Teacher's solution 

n, m = input().split() 
first = [int(i) for i in input().split()] # тут целочисленные списки
second = [int(j) for j in input().split()]

print(*sorted(set(first).intersection(second))) # если убрать * перед sorted, то вернется просто список.
# так же сортировка sorted от минимального к максимальному - это его классическая работа
"""
