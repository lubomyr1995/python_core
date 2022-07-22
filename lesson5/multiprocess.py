import math
import time
import multiprocessing
from typing import List


def time_decor(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(time.time() - start)

    return inner


def worker(num):
    res = str(math.sqrt(math.sqrt(math.sqrt((num / 2) * 5 / 15)))) + 'H'
    return res


@time_decor
def main_thread():
    print('Main')
    numbers = range(10000000)
    with open('file1.txt', 'w') as file:
        for num in numbers:
            res = worker(num)
            file.write(f'{res}\n')


# main_thread()

@time_decor
def mp():
    print('mp')
    count = multiprocessing.cpu_count()
    # print(count, 'CPU')
    if __name__ == '__main__':
        with multiprocessing.Pool(count) as p:
            numbers = range(10000000)
            with open('file.txt', 'w') as file:
                res: list = p.map(worker, numbers)
                for item in res:
                    file.write(f'{item}\n')


# mp()
