import json

import jsonpath


# 将json格式转化为Python对象
with open("book.json", "r", encoding="utf8") as f:
    obj = json.load(f)
    # result = f.read()
    # obj = json.loads(result)

# 书点所有书的作者
ret = jsonpath.jsonpath(obj, '$.store.book[*].author')
print(ret)
# print(type(ret))

# 所有的作者
ret = jsonpath.jsonpath(obj, '$..author')
print(ret)

# store的所有元素。所有的bookst和bicycle
ret = jsonpath.jsonpath(obj, '$.store.*')
print(ret)

# store里面所有东西的price
ret = jsonpath.jsonpath(obj, '$.store..price')
print(ret)

# 第三个书
ret = jsonpath.jsonpath(obj, '$.store.book[2]')
print(ret)

# 最后一本书
ret = jsonpath.jsonpath(obj, '$.store.book[(@.length-1)]')
print(ret)

# 前面的两本书
ret = jsonpath.jsonpath(obj, '$.store.book[:2]')
print(ret)

# 过滤出所有的包含isbn的书
ret = jsonpath.jsonpath(obj, '$.store.book[?(@.isbn)]')
print(ret)

# 过滤出价格低于10的书
ret = jsonpath.jsonpath(obj, '$..book[?(@.price < 10)]')
print(ret)

# 所有元素

ret = jsonpath.jsonpath(obj, '$..')
print(ret)
