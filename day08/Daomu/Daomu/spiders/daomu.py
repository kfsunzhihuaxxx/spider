# -*- coding: utf-8 -*-
import os

import scrapy

from ..items import DaomuItem


class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['www.daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']

    def parse(self, response):
        '''一级页面提取函数：提取大标题+大链接，并且把大链接交给调度器入队列'''
        a_list = response.xpath('//li[contains(@id,"menu-item-20")]/a')
        for a in a_list:
            item = DaomuItem()
            parent_title = a.xpath('./text()').get()
            parent_url = a.xpath('./@href').get()
            item['directory'] = './novel/{}/'.format(parent_title)
            # 创建文件夹
            if not os.path.exists(item['directory']):
                os.makedirs(item['directory'])
            # 交给调度器入队列
            yield scrapy.Request(url=parent_url, meta={'meta_1':item},callback=self.detail_page)

    def detail_page(self,response):
        '''二级页面解析函数：提取小标题、小链接'''
        # 把item对象接收
        meta_1 = response.meta['meta_1']
        art_list = response.xpath('//article')
        for art in art_list:
            # 只要有继续交往调度器的请求，就必须新建item对象
            item = DaomuItem()
            item['son_title'] = art.xpath('./a/text()').get()
            son_url = art.xpath('./a/@href').get()
            # 在此交给调度器入队列
            yield scrapy.Request(url=son_url,meta={'item':item},callback=self.get_content)

    def get_content(self,response):
        '''三级页面解析函数：提取具体小说内容信息'''
        item = response.meta['item']
        # content_list:['段落1','段落2','段落3',...]
        content_list = response.xpath('//article[@class="article-content"]/p/text()').extract()
        item['content'] = '\n'.join(content_list)

        #至此，一条item数据全部提取完成
        yield item