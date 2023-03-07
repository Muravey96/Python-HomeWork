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

""" Teacher's solution
VAR 1 

n = int(input())
bushes = [int(i) for i in input().split()]
bush_max = 0

for i in range(n):
    bush_sum = bushes[i - 1] + bushes[i] + bushes[i + 1 if i < n - 1 else 0]
    if bush_sum > bush_max:
            bush_max = bush_sum
 
print(bush_max)

#---------------------------------------
VAR 2 

n = int(input())
bushes = [int(i) for i in input().split()]
bush_max = 0

for i in range(-1, n - 1): # Сразу ограничение по кол-во переборов, чтоб не вылететь за границы
    bush_sum = bushes[i - 1] + bushes[i] + bushes[i + 1]
    if bush_sum > bush_max:
            bush_max = bush_sum

print(bush_max)
"""