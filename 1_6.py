ticket = int(input("Введите номер билета: "))

first_sum = 0
second_sum = 0
while ticket > 999:
    second_sum += ticket % 10
    ticket //= 10
while ticket > 0:
    first_sum += ticket % 10
    ticket //= 10

if first_sum == second_sum:
    print("Билет счастливый")
else:
    print("Не в этот раз") 




