# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scra -upy.org/en/latest/topics/items.html

import scrapy


class CrawlspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # 电影海报
    post = scrapy.Field()
    # 电影名字
    name = scrapy.Field()
    # 电影评分
    # score = scrapy.Field()
    # 电影导演
    actor = scrapy.Field()
