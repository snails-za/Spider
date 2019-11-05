# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json


class FirstbloodPipeline(object):

    # 重写这个方法，当爬虫开启的时候就会调用这个方法
    def open_spider(self, spider):
        self.fp = open('snail.txt', "a", encoding="utf8")

    # 处理item数据的方法
    def process_item(self, item, spider):
        # 要将item保存到文件中
        # 将队形转化为字典
        dic = dict(item)
        # 将字典转化为json格式
        string = json.dumps(dic, ensure_ascii=False)
        self.fp.write(string + "\n")
        return item

    #  当爬虫结束的时候调用这个方法
    def close_spider(self, spider):
        self.fp.close()
