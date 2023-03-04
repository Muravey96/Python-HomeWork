scores = {1: {'A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'},
          2: {'D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'},
          3: {'B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'},
          4: {'F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'},
          5: {'K', 'Ж', 'З', 'Х', 'Ц', 'Ч'},
          8: {'J', 'X', 'Ш', 'Э', 'Ю'},
          10: {'Q', 'Z', 'Ф', 'Щ', 'Ъ'}}
sum_score = 0
for letter in input('Введите слово: ').upper():
    for key in scores.keys():
        if letter in scores[key]:
            sum_score += key
            break
print(sum_score)