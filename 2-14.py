user_num = int(input("Введите целое число: "))

two, pow = 1, 1
while two <= user_num:
    print(two, end=" ")
    two = 2 ** pow
    pow +=1 
