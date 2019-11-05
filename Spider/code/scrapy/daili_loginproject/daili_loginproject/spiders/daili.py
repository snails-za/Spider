# -*- coding: utf-8 -*-
import scrapy


class DailiSpider(scrapy.Spider):
    name = 'daili'
    allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com/baidu?wd=ip&tn=monline_7_dg&ie=utf-8']

    def parse(self, response):
        print("*" * 50)
        with open("daili.html", "wb") as fp:
            fp.write(response.body)
        print("*" * 50)
