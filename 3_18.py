from random import randint
size = int(input('Введите размер списка: '))
numbers = tuple(randint(1, size) for _ in range(size))
print(*numbers)
num_X = int(input('Введите искомое число: '))
mod = 0
flag = False
for _ in range(len(set(numbers))):
    for i in set(numbers):
        if i == num_X - mod or i == num_X + mod:
            print(i)
            flag = True
            break
    if flag:
        break
    mod += 1


""" Teacher's var 

# --------------------------- 1 вариант
from random import randint

list_nums = [randint(1, 21) for _ in range(int(input()))] // for _ in range(int(input())) - мы указываем кол-во значений, и это же значит сколько раз мы будем обращаться к randint
                                                            а randint в свою очередь указанное в int(input() кол-во раз выдаст нам рандомное число из диапазона (1, 21)
                                                            _ (прочерк) указывается если переменная по синтаксису нужна, но в коде она не используется (мы не моежм использовать конструкцию for без переменной, но в тоже время в этом коде она нам не нужна)
print(list_nums)
num = int(input())
right_num = list_nums[0] // первое значение в списке, чтобы с него начать поиск

for i in list_nums:
    if abs(num - i) < abs(num - right_num): // abc - функция, которая возвращает модуль числа (убирает знак)
        right_num = i // переменная. куда записывается подходящее число

print(right_num)

# --------------------------- 2 вариант

from random import randint

n = int(input())
list_nums = [randint(1, 50) for _ in range(n)]

print(list_nums)

b = int(input())
m = min(list_nums, key=lambda x: abs(x - b)) // поиск минимального - смотрит все элементы списка, фиксирует разность с каждым элементом (от указанного числа)
                                                lambda - безимянная функция, генерирует ананимную функцию - https://pythonz.net/references/named/lambda/
                                                min - поиск минимального 
                                                тут нам lambda нужна, чтобы min работал так как нам надо (то есть искал не минимальное значение в списке, а минимальное с нашим условием x-b)
print(m)
"""