userNum1 = int(input("Введите 1е число: "))
userNum2 = int(input("Введите 2е число: "))


def find_pow_for_nums(x, y):
    if y == 0: return 1
    elif y == 1: return x
    return x *  find_pow_for_nums(x, y - 1)

print(find_pow_for_nums(userNum1, userNum2))