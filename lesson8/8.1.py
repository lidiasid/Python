# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона -
# данные, которые должны находиться в файле.
# 1. Программа должна выводить данные 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.

import os

file_base = "base.txt"
all_data = []
id = 0

if not os.path.exists(file_base):
    with open(file_base, "w", encoding="utf-8"):
        pass


def read_records():
    global all_data, id

    with open(file_base, "r", encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            id = int(all_data[-1].split()[0])
        return all_data


def save_records():
    with open(file_base, "w", encoding="utf-8") as f:
        f.write("\n".join(all_data))


def show_all():
    if not all_data:
        print("Empty data")
    else:
        print(*all_data, sep="\n")


def add_new_contact():
    global id
    array = ["surname", "name", "patronymic", "phone_number"]
    string = ""
    for i in array:
        string += input(f"Enter {i}: ") + " "
    id += 1
    all_data.append(f"{id} {string.strip()}")
    save_records()


def search_record():
    query = input("Enter a search query: ")
    results = [record for record in all_data if query in record]
    print(*results, sep="\n")


def delete_record():
    query = input("Enter a search query for the record you want to delete: ")
    indices = [i for i, record in enumerate(all_data) if query in record]
    if indices:
        for i in reversed(indices):
            del all_data[i]
        save_records()
        print(f"{len(indices)} record(s) deleted.")
    else:
        print("No matching records found.")


def edit_record():
    query = input("Enter a search query for the record you want to edit: ")
    indices = [i for i, record in enumerate(all_data) if query in record]
    if indices:
        for i in indices:
            print(f"Editing record: {all_data[i]}")
            new_record = input("Enter new record in format 'id surname name patronymic phone_number': ")
            all_data[i] = new_record.strip()
        save_records()
        print(f"{len(indices)} record(s) edited.")
    else:
        print("No matching records found.")


def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Delete a record\n"
                       "5. Edit a record\n"
                       "6. Exit\n")
        if answer == "1":
            show_all()
        elif answer == "2":
            add_new_contact()
        elif answer == "3":
            search_record()
        elif answer == "4":
            delete_record()
        elif answer == "5":
            edit_record()
        elif answer == "6":
            play = False
        else:
            print("Try again!\n")


main_menu()
