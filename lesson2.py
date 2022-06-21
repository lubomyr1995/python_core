# def get_rec_n(n: int):
#     if n > 1:
#         get_rec_n(n - 1)
#     print(n)
#
#
# get_rec_n(5)


# def decor(f):
#     def inner(*args, **kwargs):
#         print('********')
#         f(*args, **kwargs)
#         print('********')
#
#     return inner
#
#
# @decor
# def func(name):
#     print(f'Hello {name}')
#
#
# @decor
# def func2(name, age):
#     print(f'Hello {name} I`m {age}')
#
#
# # start = decor(func)
# # start('Ivan')
# # print()
# # decor(func2)('Ivan', 25)
#
# func('Ivan')
# print()
# func2('Ivan', 25)


# # замикання
# def counter():
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         return count
#
#     return inner
#
#
# f = counter()
# print(f())
# print(f())
# print(f())
# print(f())


# # lambda
# func = lambda x, y: x + y
# print(func(3, 5))
# lst = [1, 2, 3, 4, 5]
# m = map(lambda i: i ** 2, lst)
# print(list(m))
# print(list(map(lambda x: x ** 3, [1, 2, 3, 4, 5, 6])))


# Anotation: typehinting
# def func0(s: str) -> str:
#     return s.replace('', ',')


# from typing import Callable, List, Tuple, Dict, Optional, Union, NewType, Any, TypedDict
#
#
# # Callable - тип функції
# # Optional - параметр може бути або може не бути
# # Union - або один тип або інший
# # NewType - свій тип
#
#
# # def func1(st: str, x: int, s: bool) -> Optional[str, int]:
# def func1(st: str, x: int, s: bool) -> str | None:
#     return '1'
#
#
# # def func2(st: str, x: int, s: bool) -> Union[str, bool]:
# def func2(st: str, x: int, s: bool) -> str | bool:
#     return True
#
#
# l: List[int] = [1, 2, 3]
# t: Tuple[int, str, bool] = (1, '1', True)
# t2: Tuple[int, ...] = (1, 2, 3, 4)
# d: dict[str, str] = {'name': 'Ivan', 'surname': 'Rew'}
#
# User = TypedDict('User', {'name': str, 'age': int, 'status': bool}, total=False)
# # total - 3ій параметр означає чи всі поля обовязкові до заповнення за замовчуванням він True
# user: User = {'name': 'Ivan', 'age': 18, 'status': True}
# user2: User = {'name': 'Ivan', 'age': 18}
#
# UserId = NewType('UserId', int)
#
#
# def f(id_: UserId):
#     pass
#
#
# user_id = UserId(22)
# f(user_id)
#
#
# # Callable - першим пишеться що приймає ф-я а другим що повертає
#
#
# def counter() -> Callable[[int, str], int]:
#     count = 0
#
#     def inner(a: int, b: str) -> int:
#         nonlocal count
#         count += 1
#         return count
#
#     return inner
#
#
# counter()(2, '5')
