# # try:except
# class MyExeption(Exception):
#     pass
#
#
# try:
#     # sdsds
#     # print(22 / 0)
#     raise MyExeption
# except NameError as er:
#     print(er)
# except MyExeption:
#     print('myError')
# except Exception as err:
#     print(err)
# finally:
#     print('finish')


# generators
# g = (i for i in range(20))

# print(next(g))
# print(next(g))
# print(next(g))

# for i in g:
#     print(i)


# def gen(name):
#     for ch in name:
#         yield ch
#
#
# g = gen('Ivan')
# print(next(g))
# print(next(g))
# print('hello')
# print(next(g))
# print(next(g))


# У генератора може бути декілька yeldів
# def gen():
#     yield 1
#     yield 2
#     yield 3
#     return 'return oo'
#
#
# g = gen()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# # ////
# def gen1(n):
#     for i in range(n):
#         yield f'{i} - Team1'
#
#
# def gen2(n):
#     for i in range(n):
#         yield f'{i} - Team2'
#
#
# teams = [gen1(8), gen2(5)]
# while teams:
#     team = teams.pop(0)
#     try:
#         print(next(team))
#         teams.append(team)
#     except StopIteration:
#         pass


# # Отримання щоразу нової назви
# import uuid
#
#
# def generator_name_img():
#     pattern = '{}.jpeg'
#     while True:
#         yield pattern.format(uuid.uuid1())
#
#
# gen = generator_name_img()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


# # Робота з файлами
# try:
#     # file = open('less4.txt')
#     file = open('less4.txt', 'w')
#     try:
#         # print(file.read())
#         print(file.readlines())
#     finally:
#         file.close()
# except Exception as err:
#     print(err)


# # менеджер контекст:
# try:
#     with open('less4.txt', 'r') as file:
#         print(file.read())
# except Exception as err:
#     print(err)


# # відкриття та запис бінарних данних: в даному випадку робим копію
# try:
#     with open('lesson4.png', 'rb') as file:
#         with open('lesson4a.png', 'wb') as file2:
#             file2.write(file.read())
#
# except Exception as err:
#     print(err)


# # бібліотека pickle -- що завгодно переводить в бінарні дані
# import pickle
#
# # user = {'name': 'Max', 'age': 25}
# # try:
# #     with open('my_user', 'wb') as file:
# #         pickle.dump(user, file)
# # except Exception as err:
# #     print(err)
# try:
#     with open('my_user', 'rb') as file:
#         user = pickle.load(file)
#         print(user)
# except Exception as err:
#     print(err)


# # зберігання даних в json форматі
# import json
#
# # user = {'name': 'Max', 'age': 25}
# # try:
# #     with open('my_user.json', 'w') as file:
# #         json.dump(user, file)
# # except Exception as err:
# #     print(err)
# user = {'name': 'Max', 'age': 25}
# try:
#     with open('my_user.json', 'r') as file:
#         user = json.load(file)
#         print(user)
# except Exception as err:
#     print(err)


# # --------
# # pattern match
# # p = 1
# p = 2
#
# match p:
#     case 1:
#         print(1)
#     case 2:
#         print(2)
#     case _:
#         print('not found')
#
# # a = ['left', 200]
# a = ['top', 200]
#
# match a:
#     case 'left'|'top' as action, value:
#         print(action, value)
#     case _:
#         print('not found')
#
#
# b = ['Ivan', 26, True]
# match b:
#     case 'Ivan'|'Stepan' as action, v, True as s:
#         print(action, v, s)
#     case _:
#         print('NTF')

# user = {'name': 'Max', 'age': 25}
# match user:
#     case {'name': str(name), 'age': int(age)}:
#         print(f'name= {name}, age= {age}')
#     case _:
#         print('NF')
#
# user2 = {'name': 'Max2', 'age': 25}
# match user2:
#     case {'name': 'Max' as name, 'age': int(age)}:
#         print(f'name= {name}, age= {age}')
#     case _:
#         print('NF')


# # --------
# # match into class
# class User:
#     __match_args__ = 'name', 'age'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# user = User('Maxx', 25)
# user2 = {'name': 'Ivann', 'age': 27}
#
#
# def matcher(data: User | dict):
#     match data:
#         case User('Max' as name):
#             print(name)
#         case {'name': str(name)}:
#             print(name)
#         case _:
#             print('Nf')
#
#
# matcher(user)