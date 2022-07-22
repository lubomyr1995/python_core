import threading

# def show(n: int):
#     for i in range(n):
#         print(i, threading.current_thread().name)
#
#
# thread1 = threading.Thread(target=show, args=(5,), name='thr1', daemon=True)
# thread2 = threading.Thread(target=show, args=(9,), name='thr2', daemon=True)
#
# thread1.start()
# thread1.join()
# thread2.start()
# thread2.join()
#
# print('MainThread')


count = 0
lock = threading.Lock()


def inc():
    with lock:
        global count
        count += 1
        print(count)


threads = []
for _ in range(1000):
    thread = threading.Thread(target=inc)
    threads.append(thread)
    thread.start()

for i in threads:
    i.join()
