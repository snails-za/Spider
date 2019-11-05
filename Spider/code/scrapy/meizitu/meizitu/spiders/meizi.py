# -*- coding: utf-8 -*-
import scrapy
from meizitu.items import MeizituItem
import os


class MeiziSpider(scrapy.Spider):
    name = 'meizi'
    allowed_domains = ['www.mzitu.com']
    start_urls = ['http://www.mzitu.com/xinggan/']

    url = r'https://www.mzitu.com/xinggan/page/{}/'
    page = 1

    def parse(self, response):
        ret = response.xpath(r'//ul[@id="pins"]/li')
        item = MeizituItem()
        for oli in ret:
            image_link = oli.xpath(r'.//@data-original').extract_first()
            # print(image_link)
            image_name = oli.xpath(r'.//@alt').extract_first()
            # print(image_name)
            item["image_link"] = image_link
            item["image_name"] = image_name
            yield item
            yield scrapy.Request(url=item['image_link'], callback=self.downloader, dont_filter=True)

        if self.page < 3:
            self.page += 1
            url = self.url.format(self.page)
            # dont_filter是否过滤
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    # 下载图片的函数，referer会自动添加
    def downloader(self, response):
        dir_path = 'image'
        if not os.path.exists(dir_path):
            if not os.path.isdir(dir_path):
                os.mkdir(dir_path)
        image_link = response.url

        image_name = os.path.basename(image_link)
        # 创建图片路径
        image_path = dir_path + '/' + image_name
        with open(image_path, "wb") as f:
            f.write(response.body)


