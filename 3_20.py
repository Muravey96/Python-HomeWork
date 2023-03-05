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

""" ang_dict = {"AEIOULNSTRАВЕИНОРСТ": 1, "DGДКЛМПУ": 2,
            "BCMPБГЁЬЯ": 3, "FHVWYЙЫ": 4, "KЖЗХЦЧ": 5,
            "JXШЭЮ": 8, "QZФЩЪ": 10}

count = 0
word = input()

print(sum([i[1] for i in ang_dict.items() for j in word.upper() if j in i[0]])) 
// items - укажет и ключ и значение 
// Первый цикл - for i in ang_dict.items() перебирает значения в словаре
// второй цикл - for j in word.upper() перебирает значения в воодимом слове 
// if j in i[0] - это ключ, тоесть сравниваем букву в слове и букву в словаре, когда буква в слове и словаре совпадет, он возьмет ключ (цифру) и запишет в sum"""