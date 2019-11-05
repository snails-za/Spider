# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql


class MySqlPipeline(object):
    def open_spider(self, spider):
        # 链接数据库
        self.conn = pymysql.connect("localhost", "root", "211488", "moviedb")
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = r'insert into movie (post,name,actor) values("{}", "{}", "{}")'.format(item["post"], item["name"], item["actor"])
        # sql = r'''insert into movie value ("你好", "ckjnzzac", "zccz")'''
        self.cursor.execute(sql)

        self.conn.commit()
        print("hahaha")

    def close_spider(self, spider):
        self.conn.close()


class CrawlspiderPipeline(object):
    def open_spider(self, spider):
        self.fp = open("movie.txt", 'w', encoding='utf8')

    def process_item(self, item, spider):
        item = dict(item)
        string = json.dumps(item, ensure_ascii=False)
        self.fp.write(string + '\n')
        return item

    def close_spider(self, spider):
        self.fp.close()
