from os import path
import functions as fun
import search as sr
import change_delete as cd


file_base = "base.txt"
last_id = 0
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass

def main_menu():
    play = True
    while play:
        fun.read_records()
        answer = input("Phone book:\n"    
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change\n"
                       "5. Delete\n"
                       "6. Exit\n")
        match answer:
            case "1":
                fun.show_all()
            case "2":
                fun.add_new_contact()
            case "3":
                file_dict = sr.file_as_dict()
                sr.search_data(file_dict)
            case "4":
                cd.change_data(file_base)
            case "5":
                cd.delete_data(file_base)
            case "6":
                play = False
            case _:
                print("Try again!\n")
main_menu()