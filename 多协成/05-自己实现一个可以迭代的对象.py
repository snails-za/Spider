from collections import Iterable
from collections import Iterator
from time import sleep
class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0
    
    def add(self, name):
        self.names.append(name)


    def __iter__(self):
        """如果想要一个对象称为一个 可迭代对象，即可使用for，那么必须实现__iter__方法"""
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration
classmate = Classmate()
print(isinstance(classmate, Iterator))

classmate.add("老王")
classmate.add("王二")
classmate.add("张三")

for name in classmate:
    print(name)
    sleep(1)








