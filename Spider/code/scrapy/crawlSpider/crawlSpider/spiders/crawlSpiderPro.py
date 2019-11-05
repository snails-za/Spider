# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor  # 链接提取器
from scrapy.spiders import CrawlSpider, Rule  # spider
from crawlSpider.items import CrawlspiderItem


class CrawlspiderproSpider(CrawlSpider):
    name = 'crawlSpiderPro'
    # 允许域名
    allowed_domains = ['www.vodxc.com']
    # 起始urlhttp://www.vodxc.com/AQP/
    start_urls = ['http://www.vodxc.com/AQP/']
    # 根据规则提取所有的页码链接
    page_link = LinkExtractor(allow=r'/AQP/33-3--------.*?html',)
    detail_link = LinkExtractor(restrict_xpaths=r'//ul[@id="centertxt"]/li/h5/a')

    # 【注意】：回调函数调用方式,follow是否跟进
    rules = (
        Rule(link_extractor=page_link, follow=True),
        Rule(link_extractor=detail_link, callback='parse_item', follow=False)
    )

    # 普通的scrapy框架是parse，现在是parse_item
    def parse_item(self, response):
        item = CrawlspiderItem()
        # 名字
        item['name'] = response.xpath(r'//div[@class="vtitle"]/h1/strong/text()').extract_first()
        # 海报
        item['post'] = response.xpath(r'//div[@id="content_img"]/img/@src').extract_first()
        # 豆瓣评分
        # item['score'] = response.xpath(r'//span/p[@id="MARK_B4"]/text()').extract_first()
        # 导演
        item['actor'] = response.xpath(r'//ul/li[@class="star"]//a/@title').extract_first()
        yield item

