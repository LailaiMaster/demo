# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem

from steamSpider.models import C5ItemModel


class C5SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    price = scrapy.Field()  # 价格
    decoration_name = scrapy.Field()  # 饰品名称
    username = scrapy.Field()  # 用户名称
    decoration_id = scrapy.Field()  # 饰品id
    item_url = scrapy.Field()  # url

    pass


class C5ItemModels(DjangoItem):
    django_model = C5ItemModel

