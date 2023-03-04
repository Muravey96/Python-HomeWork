from random import randint
size = int(input('Введите размер списка: '))
nums_list = [randint(1, size) for _ in range(size)]
print(*nums_list)
print(nums_list.count(int(input('Введите искомое число: '))))