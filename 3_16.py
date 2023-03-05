from random import randint
size = int(input('Введите размер списка: '))
nums_list = [randint(1, size) for _ in range(size)]
print(*nums_list)
print(nums_list.count(int(input('Введите искомое число: '))))

""" Teacher's var

# ---------------------------1 var
list_nums = [int(input()) for _ in range(int(input()))]
print(list_nums.count(int(input())))

# --------------------------- 2 вариант

from random import choices // choices (из randome) - дает дубликаты, есть еще sample - дает уникальный набор, возвращается список значений

num = int(input()) // сбор кол-ва
list_nums = choices(range(num * 2), k=num) // формирование списка,  choices - первый аргумент, далее значения, мы увеличиваем набор значений в 2 раза range(num * 2)
                                               чтобы была возможность взять шире представленного диапазона, и choices чтобы были повторяющиеся значения. 
                                              k=num - диапазон
print(list_nums) // 

result = list_nums.count(int(input()))  // функция .count - указывается название списка (list_nums), дальше ф-я и вводим число, которое считаем (int(input())
print(result)    """