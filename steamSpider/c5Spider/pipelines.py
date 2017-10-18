# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class C5SpiderPipeline(object):
    def process_item(self, item, spider):
        print("proess item")
        print(item)
        return item

    def open_spider(self, spider):
        #一般做一些打开数据库的操作
        print("open spider")


        pass

    def close_spider(self, spider):
        print("close spider")
        pass
