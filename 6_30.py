""" Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки. """

from Modules import sequence

a = int(input('Введите первый элемент: '))
diff = int(input('Введите разность : '))
amount = int(input('Введите количество элементов: '))
print(*sequence(a, diff, amount))

# ------------Teacher's VAR -----------
first = int(input())
sub = int(input())
count = int(input())

for i in range(count):
    print(first + i * sub, end=" ")