# -*- coding: utf-8 -*-
import scrapy
from xiaohuaproject.items import XiaohuaprojectItem


class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    allowed_domains = ['wwww.521609.com']
    start_urls = ['http://www.521609.com/daxuexiaohua/']

    # 爬取每一页
    url =r'http://www.521609.com/daxuexiaohua/list3{}.html'
    page = 1

    def parse(self, response):
        li_list = response.xpath(r'//div[@class="index_img list_center"]/ul/li')

        for oli in li_list:
            item = XiaohuaprojectItem()
            image_src = oli.xpath(r'.//img/@src').extract_first()
            name = oli.xpath(r'.//img/@alt').extract_first()
            item["name"] = name
            item["image_url"] = "http://www.521609.com" + image_src
            yield item
        if self.page < 58:
            self.page += 1
            url = self.url.format(self.page)
            # dont_filter
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)







