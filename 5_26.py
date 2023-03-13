userNum1 = int(input("Введите 1е число: "))
userNum2 = int(input("Введите 2е число: "))


def find_pow_for_nums(x, y):
    if y == 0: return 1
    elif y == 1: return x
    return x *  find_pow_for_nums(x, y - 1)

print(find_pow_for_nums(userNum1, userNum2))

# -------------------------------------------------
""" Teacher's var
def pow_num(a, b):
    if b == 0: return 1
    if b < 0: return pow_num(a, b + 1) * 1 / a # Работа с отрицательной степенью, то есть возводим число в степенеь 1/а
    return pow_num(a, b - 1) * a

print(pow_num(int(input()), int(input()))) """