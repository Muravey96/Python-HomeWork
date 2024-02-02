# ------------------------------------------------

# Петя и Катя – брат и сестра. Петя – студент,
# а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает
# две подсказки. Он называет сумму этих чисел S
# и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# https://www.webmath.ru/poleznoe/formules_19_5.php

from time import time

# 1_000_000_001 1_000_000_000
s = int(input("Sum of numbers: "))
p = int(input("The product of numbers: "))
answer = "I didn't guess."

start = time()

d = s ** 2 - 4 * p

if d >= 0:
    x_1 = (s + d ** 0.5) // 2
    x_2 = (s - d ** 0.5) // 2
    if x_1 * x_2 == p:
        answer = f"{x_1}, {x_2}"

print(answer)
print(time() - start)

# -------------------- 2 вариант

s = int(input())
p = int(input())
num_1 = 1

while num_1 < p:
    num_2 = s - num_1
    if s == num_1 + num_2 and p == num_2 * num_1:
        print(num_1, num_2)
        break
    num_1 += 1


# --------------- 3 вар
# ------------------3 вариант
solutions = []
for i in range(1, 1001):
    for j in range(1, 1001):
        if s == i + j and p == i * j:
            solutions.append((min(i, j), max(i, j)))
solutions = list(set(solutions))

for solution in solutions:
    print(solution[0], solution[1])
