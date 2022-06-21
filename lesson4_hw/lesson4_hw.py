'''EX1 есть вот такой файл с email, ваша задача записать в новый текстовый файл только почты от gmail.com'''
# new_file = 'emails_gmail'
#
# try:
#     with open('emails.txt') as file_emails:
#         with open(new_file, 'w') as file_gmail:
#             for line in file_emails:
#                 if line.endswith('@gmail.com\n'):
#                     email = line.split('\t')[-1].rstrip()
#                     file_gmail.write(f'{email}\n')
#     print(f'Create file: {new_file}')
# except FileNotFoundError:
#     print(f'File {file_emails} not found!')
# except Exception as err:
#     print(err)
#
# try:
#     with open(new_file) as file:
#         print(file.read())
# except Exception as err:
#     print(err)

# # EX1 або есть вот такой файл с email, ваша задача записать в новый текстовый файл только почты от gmail.com
# RUN_FILE = 'emails.txt'
# FINISH_FILE = 'only_gmail.txt'
#
# try:
#     with open(RUN_FILE) as file, open(FINISH_FILE, 'a') as finish_file:
#         for line in file:
#             email = line.split()[-1]
#             if email.endswith('@gmail.com'):
#                 print(email, file=finish_file)
#                 # finish_file.write(f'{email}\n') - замість print може бути так
# except FileNotFoundError:
#     print(f'File {FINISH_FILE} not found!')
# except Exception as err:
#     print(err)


'''
2) для хранения и чтения данных использовать файлы

реализовать записную книжку покупок:
- каждая запись должна содержать название покупки и ее цену
-сделать менюшку для работы с записной книжкой:
    '1) Создать запись'
    '2) Список все записей'
    '3) Общая сумма всех покупок'
    '4) Самая дорогая покупка'
    '5) Поиск по названию покупки'
    '9) Выход'
- можете придумать свои пункты
'''

import json
from typing import TypedDict

ShoppingType = TypedDict('ShoppingType', {'purchase': str, 'price': int})


class Shopping:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__notes: list[ShoppingType] = []

        try:
            with open(file_name) as file:
                self.__notes: list[ShoppingType] = json.load(file)
        except:
            pass

    def add(self):
        try:
            with open(self.__file_name, 'w') as file:
                purchase = input('Input name purchase: ')
                price = int(input('Input price: '))
                self.__notes.append({'purchase': purchase, 'price': price})
                json.dump(self.__notes, file)
        except Exception as err:
            print(err)

    def show_all(self):
        if not self.__notes:
            print('No purchases yet. You can add using the add() method.')
            return
        for i in self.__notes:
            print(i)

    def price_all_purchases(self):
        sum_all = sum([i['price'] for i in self.__notes])
        print(f'{sum_all=}')

    def most_expansive_purchase(self):
        print(max(self.__notes, key=lambda i: i['price']))

    def search(self):
        find = input('Input name purchase')
        for i in self.__notes:
            if i['purchase'].lower() == find.lower():
                print(i)
                return
        print('Not find!!!')


shoping = Shopping('shopping.json')
while True:
    print(20 * '-')
    print('1) Создать запись')
    print('2) Список все записей')
    print('3) Общая сумма всех покупок')
    print('4) Самая дорогая покупка')
    print('5) Поиск по названию покупки')
    print('9) Выход')
    print(20 * '-')

    choice = input('Make your choice: ')
    match choice:
        case '1':
            shoping.add()
        case '2':
            shoping.show_all()
        case '3':
            shoping.price_all_purchases()
        case '4':
            shoping.most_expansive_purchase()
        case '5':
            shoping.search()
        case '9':
            break
