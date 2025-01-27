# multi_threaded.py
from threading import Thread




def func1():
    print("thread1")
def func2():
    print("thread2")
def func3():
    print("thread3")


t1 = Thread(target=func1)
t2 = Thread(target=func2)
t3 = Thread(target=func3)

t3.start()
t2.start()
t1.start()
# t1.join()
# t3.join()
# t2.join()

print('main thread')