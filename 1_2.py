user_num = int(input("Введите число: "))
sum = 0
while user_num>0:
    sum += user_num%10
    user_num = user_num // 10
print(sum)
