# Інкапсуляція
# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     def __set_name(self, new_name):
#         self.__name = new_name
#
#     def __get_name(self):
#         return self.__name
#
#     def __del_name(self):
#         del self.__name
#
#     my_name = property(fget=__get_name, fset=__set_name, fdel=__del_name)
#
# # або є ще простіший варіант - декоратор проперті який накладається на гетер
#
# class User2:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#
# user = User('Max')
# print(user.my_name)
#
# user2 = User2('Ivan')
# print(user2.name)
# user2.name = 'Petya'
# print(user2.name)
# del user2.name
# print(user2.name)


# # Поліморізм:
# class Shape:
#     def area(self):
#         pass
#
#     def perimetr(self):
#         pass
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def area(self):
#         return self.a * self.b * self.c / 3
#
#     def perimetr(self):
#         return self.a + self.b + self.c
#
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def area(self):
#         return self.a * self.b
#
#     def perimetr(self):
#         return (self.a + self.b) * 2
#
#
# shapes: list[Shape] = [Triangle(3, 4, 5), Rectangle(10, 20), Rectangle(3, 4)]
# for shape in shapes:
#     print(shape.area())
#     print(shape.perimetr())


# # Abstraction
# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimetr(self):
#         pass
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def area(self):
#         return self.a * self.b * self.c / 3
#
#     def perimetr(self):
#         return self.a + self.b + self.c
#
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def area(self):
#         return self.a * self.b
#
#     def perimetr(self):
#         return (self.a + self.b) * 2
#
#
# # shape = Shape() - в абстрактному методі не можна створити екземпляр класу
# shapes: list[Shape] = [Triangle(3, 4, 5), Rectangle(10, 20), Rectangle(3, 4)]
# for shape in shapes:
#     print(shape.area())
#     print(shape.perimetr())


# # staticmethod- не залежить від self, тобто не залежить від екземпляру класа
# # classmethod - cls це посилання на імя класу
# class User:
#     count = 0
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         # User.count += 1
#
#     def get_name(self):
#         return self.name
#
#     @staticmethod
#     def greeting():
#         print('Hello')
#
#     @classmethod
#     def inc_count(cls):
#         cls.count += 1
#
#     @classmethod
#     def get_count(cls):
#         return cls.count
#
#
# User.inc_count()
# User.inc_count()
# print(User.get_count())


# # Прегрузка методів
# # singleTone
# class User:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not isinstance(cls.__instance, cls):
#             cls.__instance = super().__new__(cls)
#             return cls.__instance
#         else:
#             return cls.__instance
#
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#
# user1 = User('Max')
# user2 = User('Max2')
#
# print(user1)
# print(user2)
# print(user1 is user2)


# # Перегруза метода
# # Екземпляр класу як ф-я
# class Prod:
#     def __init__(self, value, name):
#         self.name = name
#         self.value = value
#
#     def __call__(self, num):
#         self.value += num
#         return self.value
#
#
# prod = Prod(15, 'Max')
# print(prod(5))
# print(prod(5))
# print(prod.value)


# # Перегрузки
# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return str(self.__dict__)
#
#     def __repr__(self):
#         return self.__str__()
#
#     def __len__(self):
#         return len(self.name)
#
#     def __mul__(self, other):
#         return self.age * other.age
#
#
# user = User('Ivan', 25)
# print(user)
# print(len(user))

# # Создать класс Rectangle:
# # -конструктор принимает две стороны x,y
# # -описать арифметические методы:
# #   + сума площадей двух экземпляров класса
# #   - разница площадей
# #   == или площади равны
# #   != не равны
# #   >, < меньше или больше
# #   при вызове метода len() подсчитывать сумму сторон
#
# class Rectangle:
#     def __init__(self, x: int, y: int):
#         self.y = y
#         self.x = x
#         self.area = x * y
#
#     def __add__(self, other):
#         return self.area + other.area
#
#     def __sub__(self, other):
#         return self.area - other.area
#
#     def __eq__(self, other):
#         return self.area == other.area
#
#     def __ne__(self, other):
#         return self.area != other.area
#
#     def __lt__(self, other):
#         return self.area < other.area
#
#     def __gt__(self, other):
#         return self.area > other.area
#
#     def __len__(self):
#         return self.x * 2 + self.y * 2
#
#
# res1 = Rectangle(10, 10)
# res2 = Rectangle(20, 20)
#
# print(res1 + res2)
# print(res1 - res2)
# print(res1 == res2)
# print(res1 != res2)
# print(res1 < res2)
# print(res1 > res2)
# print(len(res1))
# print(len(res2))


# # создать класс Human (name, age)
# # создать два класса Prince и Cinderella:
# # у золушки должно быть имя возраст и размер ноги
# # у принца имя, возраст и размер найденной туфельки, так же должен быть метод который принимает лист золушек и ищет ту самую
# # в классе золушки должна быть переменная count которая будет считать сколько экземпляров класса золушка было создано
# # и метод класса который будет показывать это количество
#
# class Human:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
#     def __str__(self) -> str:
#         return str(self.__dict__)
#
#     def __repr__(self) -> str:
#         return self.__str__()
#
#
# class Cinderella(Human):
#     __count = 0
#
#     @classmethod
#     def inc_count(cls):
#         cls.__count += 1
#
#     @classmethod
#     def get_count(cls):
#         return cls.__count
#
#     def __init__(self, name: str, age: int, size: int):
#         super().__init__(name, age)
#         self.size = size
#         Cinderella.inc_count()
#
#
# class Prince(Human):
#     def __init__(self, name: str, age: int, size: int):
#         super().__init__(name, age)
#         self.size = size
#
#     def find_cinderella(self, cinderellas: list[Cinderella]):
#         for cinderella in cinderellas:
#             if self.size == cinderella.size:
#                 return cinderella
#         return None
#
#
# prince = Prince('Ivan', 30, 36)
# cinderellas = [Cinderella('Kira', 22, 39), Cinderella('Vika', 22, 37), Cinderella('Ira', 22, 36),
#                Cinderella('Yulia', 22, 35)]
#
# print(prince)
# print(cinderellas)
# print(prince.find_cinderella(cinderellas))
# print('cinderellas: ', Cinderella.get_count())
