# # 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# st = 'as 23 fdfdg544'
#
#
# def only_num(s):
#     l = []
#     [l.append(i) for i in s if i.isnumeric()]
#     print(','.join(l))
#
#
# only_num(st)

# # 2)написати прогу яка вибирає зі введеної строки числа і виводить їх так як вони написані
# # наприклад:
# st = 'as 23 fdfdg544 34 '
#
#
# def set_numeric(str):
#     ln = []
#     for i in str:
#         if i.isdigit() or i.isspace():
#             ln.append(i)
#     print(''.join(ln).strip().replace(' ', ', '))
#
#
# set_numeric(st)

# # 1)есть строка:
# # записать каждый символ в лист поменяв его на верхний регистр
# # пример:
# # ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
# greeting = 'Hello, world'
# lst = [i.upper() for i in greeting]
# print(lst)

# # 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# # пример:
# # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
# lst = [i ** 2 for i in range(50) if i % 2 != 0]
# print(lst)

# function
#
# # - створити функцію яка виводить ліст
# def get_list(list):
#     print(list)
#
#
# get_list([1, 2, 3])

# # - створити функцію яка приймає три числа та виводить та повертає найменьше.
# def get_min_of_three(a, b, c):
#     print(min(a, b, c))
#     return min(a, b, c)
#
#
# get_min_of_three(2, -6, -3)

# # - створити функцію яка приймає три числа та виводить та повертає найбільше.
# def get_min_of_three(a, b, c):
#     print(max(a, b, c))
#     return max(a, b, c)
#
# get_min_of_three(-4, 9, 0)

# # - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
# def get_max_ret_min(*args):
#     print(max(args))
#     return min(args)
#
#
# get_max_ret_min(1, 2, 9, -1, 20)

# # - створити функцію яка повертає найбільше число з ліста
# def get_max_of_list(lst):
#     lst.sort()
#     print(lst[-1])
#     return lst[-1]
# get_max_of_list([1,4,-2,9,-5])

# # - створити функцію яка повертає найменьше число з ліста
# def get_min_of_list(lst):
#     lst.sort()
#     print(lst[0])
#     return lst[0]
#
#
# get_min_of_list([4, -5, 5, 7])

# # - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
# def sum_list(lst):
#     s = 0
#     for i in lst:
#         s += i
#     print(s)
#     return s
#
#
# sum_list([4, -5, 5, 7])

# # - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
# def arithmetic_mean(lst):
#     print(sum(lst)/len(lst))
#     return sum(lst) / len(lst)
# arithmetic_mean([1,2,3,4,5])


# 1)Дан лист:
# #   - найти min число в листе
# list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#
# print(min(list))
# print(sorted(list)[0])

# #   - удалить все дубликаты в листе
# print(set(list))

# #   - заменить каждое четвертое значение на "Х"
# for i in range(len(list)):
#     if i % 4 == 0:
#         list[i] = 'X'
# print(list)

# # 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:
# def drow_square(n):
#     print(n * '* ')
#     for i in range(n - 2):
#         print('* ', end='');
#         print((n - 2) * '  ', end='');
#         print('*')
#     print(n * '* ')
#
#
# drow_square(5)

# # 3) вывести табличку умножения с помощью цикла while
#
#
# def multi(n):
#     i = 1
#     j = 1
#     while i < n:
#         while j < n:
#             print(i*j, end=' ')
#             j += 1
#         print()
#         i += 1
#         j = 1
#
# multi(10)


# # 4) переделать первое задание под меню с помощью цикла
# # Дан лист:
# #   - найти min число в листе
# #   - удалить все дубликаты в листе
# #   - заменить каждое четвертое значение на "Х"
#
#
# def min_el(list):
#     print('min_el: ', min(list))
#
#
# def unique(list):
#     print('unique numbers: ', set(list))
#
#
# def replase_x(list):
#     for i in range(len(list)):
#         if i % 4 == 0:
#             list[i] = 'X'
#     print('modified list: ', list)
#
#
# while True:
#     list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#     print('1. Знайти мін число.\n2. Видалити всі одинакові значення.\n3. Замінити кожне 4-е значення на Х:\n0. Вийти з програми')
#     k = int(input())
#     if k == 1:
#         min_el(list)
#     elif k == 2:
#         unique(list)
#     elif k == 3:
#         replase_x(list)
#     elif k == 0:
#         break
#     print('Зробіть свій вибір')

