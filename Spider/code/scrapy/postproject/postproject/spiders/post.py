# -*- coding: utf-8 -*-
import scrapy


class PostSpider(scrapy.Spider):
    name = 'post'
    allowed_domains = ['fanyi.baidu.com/?aldtype=16047#auto/zh']
    # start_urls = ['http://fanyi.baidu.com/?aldtype=16047#auto/zh/']
    def start_requests(self):
        post_url = r'http://fanyi.baidu.com/sug'
        # 表单数据
        form_data = {'kw': 'wolf'}
        # 发送请求
        yield scrapy.FormRequest(url=post_url, formdata=form_data, callback=self.parse)

    def parse(self, response):
        print("*" * 50)
        print(response.text)
        print("*" * 50)

