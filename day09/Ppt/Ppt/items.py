# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PptItem(scrapy.Item):
    # define the fields for your item here like:
    # 思考定义哪些字段(pipeline.py中需要哪些)：大分类名字、ppt模板的名字、ppt的下载链接
    parent_name = scrapy.Field()
    ppt_name = scrapy.Field()
    ppt_download = scrapy.Field()