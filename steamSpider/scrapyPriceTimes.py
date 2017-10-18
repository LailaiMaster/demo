import os
from concurrent.futures import ThreadPoolExecutor, wait
from urllib import request
import requests
import re
from urllib.parse import urljoin
import json
from bs4 import BeautifulSoup


class CrawlThreadPool(object):
    def __init__(self):
        self.thread_pool = ThreadPoolExecutor(max_workers=5)

    def _request_parse_runnable(self, url):
        try:
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"}
            req = request.Request(url, headers=headers)
            content = request.urlopen(req).read().decode("utf-8")
            soup = BeautifulSoup(content, "lxml", from_encoding='utf-8')
            links = soup.select('.sale-item-lists > ul > li > a')
            saleLink = links[0]
            marketUrl = 'https://www.c5game.com' + saleLink.get('href')
            priceSourceCode = str(request.urlopen(marketUrl).read())
            # print(marketUrl)
            priceSoup = BeautifulSoup(priceSourceCode, 'lxml')
            # print(priceSoup)
            price = priceSoup.select('.tab-content > #sale > table > #sale-table')[0]
            jsUrl = price.get('data-url')
            allUrl = "https://www.c5game.com" + jsUrl
            # req = request.Request(allUrl, headers=headers)
            response = requests.get(allUrl)
            data = json.loads(response.text)
            body = data["body"]
            items = []
            for i in body['items']:
                items.append(i)
        except BaseException as e:
            print(str(e))
            items = []
        return items

    def _igxe_request_parse_runnable(self, url):
        try:
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"}
            req = request.Request(url, headers=headers)
            cookies = {"csrftoken": "ulcj4TBxWUibMOew4o52CdFHKFA9XVKT", "expires": "Tue, 16-Oct-2018 08:56:45 GMT",
                       "Max-Age": "31449600", "Path": "", "sessionid": "i7v1lxnsx9buhj9756yri6xm5pba8hz2",
                       "httponly": "", "Path": ""}
            response = requests.get(url, headers=headers, cookies=cookies)
            # content = request.urlopen(req).read().decode("utf-8")
            soup = BeautifulSoup(response.text, "lxml", from_encoding='utf-8')
            # print(soup)
            jsUrl = re.search("/.*trade/\d*.\d*", soup.get_text()).group()
            allUrl = "https://www.igxe.cn" + jsUrl + "?page_no=1&gem_id=0&gem_attribute_id=0"
            print(allUrl)
            response = requests.get(allUrl)
            data = json.loads(response.text)
            print(data)
            items = []
            d_list = data["d_list"]
            for i in d_list:
                d = {"name": i["name"], "price": i["unit_price"]}
                items.append(d)
        except BaseException as e:
            print(str(e))
            items = []
        return items

        # def crawl(self, url, complete_callback):
        #     future = self.thread_pool.submit(self._request_parse_runnable, url)
        #     future.add_done_callback(complete_callback)


class CrawlManager(object):
    '''
    爬虫管理类，负责管理爬取解析线程池及存储线程池
    '''

    def __init__(self):
        self.crawl_pool = CrawlThreadPool()

    def _crawl_future_callback(self, crawl_url_future):
        try:
            data = crawl_url_future.result()
            print(data)
        except Exception as e:
            print('Run crawl url future thread error. ' + str(e))

    def start_runner(self, c5, igxe):
        c5Results = self.crawl_pool.thread_pool.map(self.crawl_pool._request_parse_runnable, c5)
        igxeResults = self.crawl_pool.thread_pool.map(self.crawl_pool._igxe_request_parse_runnable, igxe)
        # for url in urls:
        #     self.crawl_pool.crawl(url, self._crawl_future_callback)
        return {"c5": c5Results, "igxe": igxeResults}


def scrape():
    c5 = ["https://www.c5game.com/market/578080-553383771-S.html",
          "https://www.c5game.com/market/578080-553383768-S.html",
          "https://www.c5game.com/market/578080-553383769-S.html",
          "https://www.c5game.com/market/578080-553383767-S.html",
          "https://www.c5game.com/market/578080-553383770-S.html",
          ]

    igxe = ["https://www.igxe.cn/product/578080/602957",
            "https://www.igxe.cn/product/578080/602945",
            "https://www.igxe.cn/product/578080/602955",
            "https://www.igxe.cn/product/578080/602939",
            "https://www.igxe.cn/product/578080/602940",
            ]
    # result = CrawlManager().start_runner(root_url)
    # for r in result:
    # print(r)
    return CrawlManager().start_runner(c5=c5, igxe=igxe)
