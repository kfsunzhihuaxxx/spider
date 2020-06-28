# -*- coding: utf-8 -*-
import scrapy


class GuaziSpider(scrapy.Spider):
    name = 'guazi'
    allowed_domains = ['www.guazi.com']
    # 其实的url地址，需要改为 第一页的url地址
    start_urls = ['https://www.guazi.com/zz/buy/']

    def parse(self, response):
        '''response为第一页的响应对象，提取具体数据'''
        # li_list:[<Selector1>,<Selector2>,...<Selector40>]
        li_list = response.xpath('//ul[@class="carlist clearfix js-top"]/li')
        for li in li_list:
            item={}
            item['name'] = li.xpath('./a[1]/@title').get()
            item['link'] = li.xpath('./a[1]/@href').get()
            print(item)