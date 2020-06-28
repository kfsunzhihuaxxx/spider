'''
线程锁使用示例：

'''

from threading import Thread, Lock

n = 5000
lock = Lock()

def f1():
    global n
    for i in range(1000000):
        lock.acquire()
        n = n + 1
        lock.release()

def f2():
    global n
    for i in range(1000000):
        lock.acquire()
        n = n - 1
        lock.release()

t1 = Thread(target=f1)
t1.start()

t2 = Thread(target=f2)
t2.start()

t1.join()
t2.join()
print(n)

