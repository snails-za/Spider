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
        return ClassIterator()


class ClassIterator(object):
    def __iter__(self):
        pass

    def __next__(self):
        return 11


classmate = Classmate()


classmate.add("老王")
classmate.add("王二")
classmate.add("张三")

print("判断classmate是否是可迭代对象：", isinstance(classmate, Iterable))
classmate_iterator = iter(classmate)
print("判断class_iterator是否是迭代器：", isinstance(classmate_iterator, Iterable))

print(next(classmate_iterator))
for name in classmate:
    print(name)
    sleep(1)








