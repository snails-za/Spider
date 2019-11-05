# -*- coding: utf-8 -*-
import scrapy
from firstblood.items import FirstbloodItem

class SnailSpider(scrapy.Spider):
    name = 'snail'
    allowed_domains = ['www.win4000.com/mobile.html']
    start_urls = ['http://www.win4000.com/mobile.html/']

    # 解析函数,重写这个方法，发送请求之后，响应来了就会调用这个方法，函数有一个函数response就是响应内容，
    # 该函数对返回值有一个要求，必须返回可迭代对象
    def parse(self, response):
        # print("嘿嘿嘿")
        print(type(response))
        # print(response.text)
        # print(response.body)
        img_list = response.xpath(r'//div[@class="list_cont list_cont2 w1180"]//ul[@class="clearfix"]//li//img/@src').extract()
        title_list = response.xpath(r'//div[@class="list_cont list_cont2 w1180"]//ul[@class="clearfix"]//li//img/@title').extract()
        # print(img_list)
        # print(title_list)
        item = FirstbloodItem()
        for img, title in zip(img_list, title_list):
            item["img"] = img
            item["title"] = title
            yield item
            # item = {
            #     "图片": img,
            #     "题目": title
            # }
            # items.append(item)

        # print("哈哈哈")

