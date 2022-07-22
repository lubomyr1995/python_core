# gen = (i for i in range(2, 10001))
# for i in gen:
#     print(i)


# a, b = map(int, input().split())
# gen = (i**2 for i in range(a, b + 1))
# tp = tuple(i for i in gen)
# print(tp)


# a, b = map(int, input().split())
# gen = (abs(i) for i in range(a, b + 1))
# j = 5
# for i, v in enumerate(gen):
#     if i > 4:
#         break
#     print(v)


# a, b = map(int, input().split())
# gen = (abs(x) for x in range(a, b + 1))
# for i in range(5):
#     print(next(gen))


# a = int(input())
# gen = (abs(i**3) for i in range(-a, a))
# for i in range(4):
#     print(next(gen), end=' ')


# from string import ascii_lowercase
#
# gen = (i+j for i in ascii_lowercase for j in ascii_lowercase)
#
# for i in range(50):
#     print(next(gen), end=' ')


# cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
# gen = (i for i in cities*166667)
# for i in range(20):
#     print(next(gen), end=' ')


# a, b = map(int, input().split())
# gen = (round((0.5 * pow((i / 100), 2) - 2), 2) for i in range(a * 100, b * 100))
# for i in range(20):
#     print(next(gen), end=' ')


# def gen():
#     for i in range(1, 10):
#         a = range(i, 11)
#         yield sum(a) / len(a)
#
#
# g = gen()
# print(*(list(g)))


# N = int(input())
# def get_sum(N):
#     for i in range(1, N + 1):
#         s = range(i + 1)
#         yield sum(s)
# print(list(get_sum(N)))


# lst = map(float, input().split())
# print(*(next(lst) for i in range(3)))


# lst = map(lambda x: abs(int(x)), input().split())
# print(*lst)


# import sys
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# lst2D = list(map(lambda x: list(map(int, x.split(' '))), lst_in))
# # lst2D = [list(map(int, i.split())) for i in lst_in]
# print(*lst_in)
# print(*lst2D)

# print(*map(lambda x: '-' if len(x) < 5 else x, input().split()))


