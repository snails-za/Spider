# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import urllib.request


class XiaohuaprojectPipeline(object):
    def open_spider(self, spider):
        self.image_dir = r'image'
        if not os.path.exists(self.image_dir):
            if not os.path.isdir(self.image_dir):
                os.mkdir(self.image_dir)

    def process_item(self, item, spider):
        self.download_image(item)

    def download_image(self, item):
        image_name = item["name"] + ".jpg"
        image_path = os.path.join(self.image_dir, image_name)
        urllib.request.urlretrieve(item["image_url"], image_path)

