from collections import Iterable
from collections import Iterator
from time import sleep
class Classmate(object):
    def __init__(self):
        self.names = list()

    
    def add(self, name):
        self.names.append(name)


    def __iter__(self):
        """如果想要一个对象称为一个 可迭代对象，即可使用for，那么必须实现__iter__方法"""
        return ClassIterator(self)


class ClassIterator(object):
    def __init__(self, obj):
        self.obj = obj
        self.current_num = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.current_num < len(self.obj.names):
            ret = self.obj.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration
classmate = Classmate()

classmate.add("老王")
classmate.add("王二")
classmate.add("张三")

for name in classmate:
    print(name)
    sleep(1)








