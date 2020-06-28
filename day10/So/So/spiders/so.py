# -*- coding: utf-8 -*-
import json

import scrapy
from ..items import SoItem

class SoSpider(scrapy.Spider):
    name = 'so'
    allowed_domains = ['image.so.com']
    # 重写一下start_requests()方法
    def start_requests(self):
        url = 'https://image.so.com/zjl?ch=beauty&sn={}&listtype=new&temp=1'
        for i in range(6):
            sn = i * 30
            page_url = url.format(sn)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        '''提取数据：提取图片名称和链接'''
        html = json.loads(response.text)
        for one_img in html['list']:
            item = SoItem()
            item['title'] = one_img['title']
            item['imgurl'] = one_img['qhimg_url']

            #吧item对象交给管道文件处理
            yield item
