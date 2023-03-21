from os import path

file_base = "base.txt"
last_id = 0
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass 

def file_as_dict():
    global file_base
    with open(file_base, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = ['ID', 'Surname', 'Name', 'Patronymic', 'Phone_number']
    contact_list = []
    for line in lines:
        line = line.strip().split()
        contact_list.append(dict(zip(headers, line)))
    return contact_list

def search_param():
    print('Search parameter: ')
    param = input("1 - ID\n"
                  "2 - Surname\n"
                  "3 - Name\n"
                  "4 - Patronymic\n"
                  "5 - Phone_number\n")
    value = None
    if param == '1':
        value = input('Print ID: ')
        print()
    elif  param == '2':
        value = input('Print Surname: ')
        print()
    elif  param == '3':
        value = input('Print Name: ')
        print()
    elif  param == '4':
        value = input('Print Patronymic: ')
        print()
    elif  param == '5':
        value = input('Print Phone_number: ')
        print()
    return param, value 
    

def search_data(file_dict):
    param, value = search_param()
    value_dict = {'1': 'ID', '2': 'Surname', '3': 'Name', '4': 'Patronymic', '5': 'Phone_number'}
    found_data = []
    for contact in file_dict:
        if contact[value_dict[param]] == value:
            found_data.append(contact)
    if len(found_data) == 0:
        print("No such contacts was found")
    else: 
        print(found_data)
    print()
    
        

