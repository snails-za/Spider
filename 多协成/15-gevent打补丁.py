import gevent
import time
from gevent import monkey

monkey.patch_all()


def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)

def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)
def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)



g1 = gevent.spawn(f1, 5)
g2 = gevent.spawn(f2, 5)
g3 = gevent.spawn(f3, 5)
g1.join()
g2.join()
g3.join()
