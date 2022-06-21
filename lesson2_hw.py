# # EX1: написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
# # - первый записывает в эту переменную запись
# # - второй возвращает все записи
# # запишите 5 тудушек и выведете все
#
# def notebook():
#     todo_list = []
#
#     def add__todo(todo):
#         todo_list.append(todo)
#
#     def get__all():
#         return todo_list
#
#     return add__todo, get__all
#
#
# add_todo, get_all = notebook()
# add_todo('do1')
# add_todo('do2')
# add_todo('do3')
# add_todo('do4')
# add_todo('do5')
# print(get_all())


# # EX2) протипизировать первое задание
# from typing import Callable, Tuple, List
#
#
# def notebook_a() -> tuple[Callable[[str], None], Callable[[], list[str]]]:
#     lst: list = []
#
#     def add__todo(todo: str) -> None:
#         lst.append(todo)
#
#     def get__all() -> list[str]:
#         return lst
#
#     return add__todo, get__all
#
#
# add_todo, get_all = notebook_a()
# add_todo('doo1')
# add_todo('doo2')
# add_todo('doo3')
# add_todo('doo4')
# add_todo('doo5')
# print(get_all())


# # EX3) создать функцию которая будет возвращать сумму разрядов числа в виде строки (тоже с типизацией)
# # Пример:
# # expanded_form(12) # return '10 + 2'
# # expanded_form(42) # return '40 + 2'
# # expanded_form(70304) # return '70000 + 300 + 4'
# def expanded_form(n: int) -> str:
#     st = str(n)
#     lst = []
#     for i, j in enumerate(st):
#         if j != '0':
#             lst.append(f'{j}{("0" * (len(st) - i - 1))}')
#     return '+'.join(lst)
#
#
# print(expanded_form(42))
# print(expanded_form(142))
# print(expanded_form(70304))


# # EX4 создать декоратор который будет считать сколько раз была запущена функция
# # и будет выводит это значение после каждого запуска функции
# from typing import Callable
#
#
# def dec(f: Callable) -> Callable:
#     counter = 0
#
#     def inner() -> None:
#         nonlocal counter
#         counter += 1
#         print('Викликів ф-ї: ', counter)
#         f()
#         print(10 * ' *')
#
#     return inner
#
#
# @dec
# def say_hello() -> None:
#     print('Hello')
#
#
# say_hello()
# say_hello()
# say_hello()
# say_hello()


# # EX5 сделайте функцию на замыкания которая будет возвращать декоратор который будет считать
# # общее количество запущенных  функций декорированных этим декоратором
# from typing import Callable
#
#
# def func_dec():
#     counter = dict()
#
#     def dec(f: Callable) -> Callable:
#         nonlocal counter
#         counter[f] = 0
#
#         def inner():
#             counter[f] += 1
#             print('count: ', sum(counter.values()))
#             f()
#             print(20 * '-')
#
#         return inner
#
#     return dec
#
#
# decor = func_dec()
#
#
# @decor
# def func1() -> None:
#     print('func1')
#
#
# @decor
# def func2() -> None:
#     print('func2')
#
#
# func1()
# func1()
# func2()
# func2()
