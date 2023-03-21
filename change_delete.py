from os import path
import search as sr

file_base = "base.txt"
last_id = 0
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass

def file_as_list(file_base):
    with open(file_base, 'r', encoding='utf-8') as file:
        file_list = []
        for line in file.readlines():
            file_list.append(line.split())
    return file_list

def search_modify(file_base: list):
    param, value = sr.search_param()
    result = []
    for contact in file_base:
        if contact[int(param) -1] == value:
            result.append(contact)
    if len(result) ==1 :
        return result[0]
    elif len(result) > 1:
        print("Found several contacts")
        for i in range(len(result)):
            print(f'{i + 1} - {result[i]}')
        choose_num = int(input('Choose ID to change\delete: '))
        return result[choose_num - 1]
    else: 
        print('No such contacts was found')
    print()


def change_data(file):
    file_list = file_as_list(file)
    contact_to_change = search_modify(file_list)
    file_list.remove(contact_to_change)
    print('Data to change: ')
    answer = input('1 - Surname\n'
                   '2 - Name\n'
                   '3 - Patronymic\n'
                   '4 - Phone_number\n')
    if answer == '1':
        contact_to_change[1] = input('Print Surname: ')
    elif answer == '2':
        contact_to_change[2] = input('Print Name: ')
    elif answer == '3':
        contact_to_change[3] = input('Print Patronymic: ')
    elif answer == '4':
        contact_to_change[4] = input('Print Phone_number: ')
    file_list.append(contact_to_change)
    with open(file, 'w', encoding='utf-8') as f:
        for contact in file_list:
            line = ' '.join(contact) + '\n'
            f.write(line)

def delete_data(file):
    file_list = file_as_list(file)
    contact_to_change = search_modify(file_list)
    file_list.remove(contact_to_change)
    with open(file, 'w', encoding='utf-8') as f:
        for contact in file_list:
            line = ' '.join(contact) +'\n'
            f.write(line)
