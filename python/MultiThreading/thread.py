from threading import *
from time import sleep
class hello(Thread):
    def run(self):
        for i in range(5):
            print('Hello')
            sleep(2)

class hi(Thread):
    def run(self):
        for i in range(5):
            print('Hi')
            sleep(2)

t1 = hello()
t2 = hi()

t1.start()
t2.start()

t1.join()
t2.join()
print("Bye")