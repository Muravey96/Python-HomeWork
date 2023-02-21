length = int(input('Длина шоколадки: '))
width = int(input('Ширина шоколадки: '))
num_of_pieces = int(input('Количество долек: '))
if (num_of_pieces % length == 0 or num_of_pieces % width == 0) and  num_of_pieces < length * width:
    print(f'Вы можете отломить от шоколадки {num_of_pieces} долек')
else:
    print(f'Вы не можете отломить от шоколадки {num_of_pieces} долек')