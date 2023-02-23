""" 
x + y = S => x = S - y
xy = y(S-y) = P => y^2 - Sy + P = 0
D = S^2-4P 
Поиск через дискриминант"""

sum = int(input("Введите сумму: "))
product = int(input("Введите произведение: "))

y1 = (sum + (sum ** 2 - 4 * product) ** 0.5 ) / 2
y2 = (sum - (sum ** 2 - 4 * product) ** 0.5 ) / 2
x1 = sum - y1
x2 = sum - y2

if y1 > 0 and x1 > 0:
    print(f'Первое число = {x1}, второе число = {y1}')
if y2 > 0 and x2 > 0 and y2 != y1 and x2 != x1 and y2 != x1 and x2 != x1:
    print(f'Первое число = {x2}, второе число = {y2}')