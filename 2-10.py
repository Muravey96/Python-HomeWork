coins = int(input("Введите количество монет: "))
count_1, count_0 = 0, 0

for i in range(coins):
    side = int(input("Орел (1) или Решка (0)?: "))
    if side == 0:
        count_0 += 1
    else:
        count_1 += 1
print()
if count_0 >= count_1:
    print(f"Необходимо перевернуть {count_1} монет/ы")
else:
    print(f"Необходимо перевернуть {count_0} монет/ы")