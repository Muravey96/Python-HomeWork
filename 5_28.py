userNum1 = int(input("Введите 1е число: "))
userNum2 = int(input("Введите 2е число: "))

def numbers_sum(x, y):
    if y > x: x, y = y, x
    elif y == 0: return x
    return x + numbers_sum(x, y -1)

print(numbers_sum(userNum1, userNum2))