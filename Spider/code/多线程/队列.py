
from queue import Queue


# 创建队列
q = Queue(5)
print(q.empty())
print(q.full())
print(q.qsize())
# 存数据
q.put("科比")
q.put("勒布朗")
q.put("JR")
q.put("汤普森")
q.put("love")
# q.put("乔治希尔", True, 3)
# # print(q)
print(q.empty())
print(q.full())
print(q.qsize())
# 取数据
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())

print(q.get(True, 3))






