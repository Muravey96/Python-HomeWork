def sequence(a:int, diff:int, amount:int):
    sequence = [a]
    for i in range(2, amount + 1):
        sequence.append(a + (i - 1) * diff)
    return sequence

from random import randint
def create_list(x: int):
    my_list = []
    for _ in range(x):
        my_list.append(randint(1, 50))
    return my_list


def indexes_search(num: list, min: int, max: int):
    indexes_list = []
    for i in range(len(num)):
        if min <= num[i] <= max:
            indexes_list.append(i)
    return indexes_list