# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной


from csv import DictWriter, DictReader
from os.path import exists

def create_file():
    with open('phone.csv', 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()

def get_info():
    info = []
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    info.append(last_name)
    info.append(first_name)
    flag = False
    while not flag:
        try:
            phone_number = int(input('Введите номер телефона: '))
            if len(str(phone_number)) != 11:
                print('Неправильный номер, введите правильный номер!')
            else:
                flag = True
        except ValueError:
            print('not valid number')
    info.append(phone_number)
    return info

def write_file(lst):
    with open('phone.csv', 'r+', encoding='utf-8', newline='') as data:
        f_reader = DictReader(data)
        res = list(f_reader)
    with open('phone.csv', 'w', encoding='utf-8', newline='') as data:
        obj = {'Фамилия': lst[0], 'Имя': lst[1], 'Номер': lst[2]}
        res.append(obj)
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()
        for el in res:
            f_writer.writerow(el)

def read_file(file_name):
    with open(file_name, encoding='utf-8') as data:
        f_reader = DictReader(data)
        res = list(f_reader)
    return res

def record_info(info):
    lst = get_info()
    write_file(lst)

def search_info(file_name):
    last_name = input('Введите фамилию или имя: ')
    with open(file_name, encoding='utf-8') as data:
        f_reader = DictReader(data)
        phone_info = list(f_reader)
        count = 0
        position_record = []
        for i in range(len(phone_info)):
            for k, v in phone_info[i].items():
                if v == last_name:
                    print(i, phone_info[i])
                    count += 1
                    position_record.append(i)
    if count == 0:
        print('По вашему запросу ничего не найдено.')
        print()

def edit_record(edit_num):
    with open('phone.csv', 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
        res = list(f_reader)
        print(edit_num, res[edit_num])
        print('Введите новые данные контакта:')
        obj = get_info()
        obj_edited = {'Фамилия': obj[0], 'Имя': obj[1], 'Номер': obj[2]}
        res.pop(edit_num)
        res.insert(edit_num, obj_edited)
    with open('phone.csv', 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()
        for el in res:
            f_writer.writerow(el)

def delete_record(delete_num):
    with open('phone.csv', 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
        res = list(f_reader)
    with open('phone.csv', 'w', encoding='utf-8', newline='') as data:
        res.pop(delete_num)
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()
        for el in res:
            f_writer.writerow(el)

def main():
    while True:
        command = input('Введите команду:\n q - выход (quit)\n r - открыть справочник (read)\n a - добавить контакт (add)\n'
                        ' s - поиск контакта (search)\n d - удалить контакт (delete)\n e - изменить контакт (edit)\n')
        if command == 'q':
            break
        elif command == 'r':
            if not exists('phone.csv'):
                print('Файл не создан')
                break
            rst = read_file('phone.csv')
            for i in range(len(rst)):
                print(i, end=" ")
                for k, v in rst[i].items():
                    print(k + ': ', v, end=' ')
                print()
        elif command == 'a':
            if not exists('phone.csv'):
                create_file()
                write_file(get_info())
            else:
                record_info('phone.csv')
        elif command == 's':
            search_info('phone.csv')
        elif command == 'd':
            delete_num = int(input('Введите номер удаляемой записи: '))
            delete_record(delete_num)
        elif command == 'e':
            edit_num = int(input('Введите номер редактируемой записи: '))
            edit_record(edit_num)

main()
