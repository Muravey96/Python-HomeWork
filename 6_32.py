""" Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума) """

from Modules import create_list, indexes_search


num_list = create_list(int(input('Введите размер массива: ')))
left_stop = int(input('Введите минимум диапазона: '))
right_stop = int(input('Введите максимум диапазона: '))

print(*num_list)
print(*indexes_search(num_list, left_stop, right_stop))