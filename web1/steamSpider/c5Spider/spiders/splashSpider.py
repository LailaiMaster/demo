# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

from steamSpider.c5Spider.items import C5SpiderItem, C5ItemModels

__author__ = 'Jian Lee'


class igxeSplashSpiderS(scrapy.Spider):
    name = "igxe-s"
    start_urls = ["https://www.igxe.cn/pubg/578080/product-602957",
                  "https://www.igxe.cn/pubg/578080/product-602945",
                  "https://www.igxe.cn/pubg/578080/product-602955",
                  "https://www.igxe.cn/pubg/578080/product-602939",
                  "https://www.igxe.cn/pubg/578080/product-602940", ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 1})

    def parse(self, response):
        print(response.xpath('/html/head/title/text()').extract())
        print(response.xpath('//*[@id="js-tbody-data"]/tr/td[3]/span/text()').extract())
        print(response.xpath('//*[@id="js-tbody-data"]/tr[1]/td[1]/a[1]/span/text()').extract())


class SplashSpiderS(scrapy.Spider):
    name = "c5-s"
    # start_urls = ["https://item.jd.com/11022355451.html"]
    start_urls = ["https://www.c5game.com/market/578080-553383771-S.html",
                  "https://www.c5game.com/market/578080-553383768-S.html",
                  "https://www.c5game.com/market/578080-553383769-S.html",
                  ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                                args={'wait': 1, })

    def parse(self, response):

        price = response.xpath('//*[@id="sale-table"]/tr/td[3]/span/text()').extract()  # 价格
        name = response.xpath('//div[@class="name"]/text()')[0].extract()  # 饰品名称
        print(price)
        count = 0
        print(name)

        for p in price:
            item = C5ItemModels()
            item['price'] = p
            item['decoration_id'] = count
            item['decoration_name'] = name
            item['item_url'] = "www"
            item['data_type'] = "c5"
            item.save()
            count += 1
            if count > 4:
                return
            print(item)
            print('保存完了')

            # if item['price']:
            #     print("list不为空")
            # else:
            #     print("没有获取到价格" + response.url)
            #     yield SplashRequest(response.url, self.parse_price, callback=self.test)
            #
            #
            # def test(self):
            #     print("== 测试回调===")
            #     pass
            #
            # def parse_price(self, response):
            #     print("===重新获取价格=====%s" % response.url)
            #
            #     price = response.xpath('//*[@id="sale-table"]/tr/td[3]/span/text()').extract()  # 价格
            #     print(price)
            #
            #     pass


class SplashSpiderP(scrapy.Spider):
    name = "c5-p"
    # start_urls = ["https://item.jd.com/11022355451.html"]
    start_urls = ["https://www.c5game.com/market/578080-553383771-P.html",
                  # "https://www.c5game.com/market/578080-553383768-P.html",
                  # "https://www.c5game.com/market/578080-553383769-P.html",
                  ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 1})

    def parse(self, response):
        print("==========")
        print(response.url)
        print(response.xpath('///*[@id="buy"]/table/tbody[2]/tr/td[4]/span/text()').extract())  # 静态获取不到价格。
        print(response.xpath('//div[@class="name"]/text()')[0].extract())  # c5的标题
        pass



        #
        # print(response.xpath('//span[@class="ft-orange"]/text()').extract())  静态获取不到价格。
        # print(response.xpath('//div[@class="sku-name"]/text()')[0].extract()) jd的标题
        # print(response.xpath('//div[@class="name"]/text()')[0].extract()) #c5的标题
