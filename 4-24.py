from random import randint
berry_num = [randint(0, 20) for i in range(int(input('Введите количество кустов: ')))]
print(*berry_num)
max_berries = 0
for i in range(len(berry_num)):
    if i == len(berry_num) - 1:
        total_berries = berry_num[i - 1] + berry_num[i] + berry_num[0]
    else:
        total_berries = berry_num[i - 1] + berry_num[i] + berry_num[i + 1]
    max_berries = total_berries if total_berries > max_berries else max_berries
print(max_berries)