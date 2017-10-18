# -*- coding: utf-8 -*-
from scrapy import cmdline

__author__ = 'Jian Lee'


# 调试文件 name就是我们爬虫的name 右键debug run 就好了



def runSpider():
    print("==========")
    name = 'c5-s'
    cmd = 'scrapy crawl {0}'.format(name)
    cmdline.execute(cmd.split())


print("====run.py====")
runSpider()

# runSpider()
# scrapy crawl huxiu -o items.json
