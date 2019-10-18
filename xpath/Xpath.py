from lxml import etree
from collections import Iterable

# 生成对象
tree = etree.parse('xpath.html')

# print(tree)

"""取文本，取属性"""
# ret = tree.xpath(r'//div[@class="tang"]/ul/li[1]/text()')
# print(ret)
# ret = tree.xpath(r'//div[@class="tang"]/ul/li[1]/@class')
# print(ret)
"""层次定位，索引定位"""
# ret = tree.xpath(r'//div[@class="tang"]/ul/li[@class="love"]')
# print(ret)
"""逻辑运算"""
# ret = tree.xpath(r'//div[@class="tang"]/ul/li[@class="love" and @name="yang"]')
# print(ret)
"""模糊查询"""
# ret = tree.xpath(r'//div[@class="tang"]/ol/li[contains(@class, "lily")]/text()')
# print(ret)
# ret = tree.xpath(r'//li[contains(text(), "爱")]/text()')
# print(ret)
# ret = tree.xpath(r'//li[starts-with(@class, "ba")]/text()')
# print(ret)

"""取文本"""
ret = tree.xpath(r'//div[@class="song"]/text()')
print(ret)
ret = tree.xpath(r'//div[@class="song"]//text()')
print(ret)

# ret = tree.xpath(r'//div[@class="song"]')
# string = ret[0].xpath('string(.)')
"""简写"""
string = tree.xpath(r'string(//div[@class="song"])')
print(string)
print(string)
print(type(string))
print("可迭代：", isinstance(string, Iterable))
string_list = string.replace('\t', "").strip('\n').split("\n")
print(string_list)
for s in string_list:
    print(s)



