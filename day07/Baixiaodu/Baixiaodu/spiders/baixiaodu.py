# -*- coding: utf-8 -*-
import scrapy


class BaixiaoduSpider(scrapy.Spider):
    name = 'baixiaodu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        """解析提取所需数据"""
        # Scrapy中相应对象response可以直接调用xpath

        # 1. response.xpath() 结果：[Selector xpath='' data='字符串']
        # 2. extract() 结果：['百度一下，你就知道'] 提取出selector对象的字符串
        # 3. extract_first() 结果：'百度一下，你就知道'
        # 4. get() 结果：'百度一下，你就知道'
        result = response.xpath('/html/head/title/text()').extract_first()
        result = response.xpath('/html/head/title/text()').get()
        # ["百度一下，你就知道"]
        print(result)
        print("*"*50)
