from django.db import models


# Create your models here.


class C5ItemModel(models.Model):
    # price = scrapy.Field()  # 价格
    # decoration_name = scrapy.Field()  # 饰品名称
    # username = scrapy.Field()  # 用户名称
    # decoration_id = scrapy.Field()  # 饰品id
    # item_url = scrapy.Field()  # url

    price = models.CharField(max_length=20, null=True)
    decoration_name = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50, null=True)
    decoration_id = models.CharField(max_length=20, null=True)
    item_url = models.CharField(max_length=50, null=True)
    data_type = models.CharField(max_length=20, null=True)
