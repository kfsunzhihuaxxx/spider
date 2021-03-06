# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KfcItem(scrapy.Item):
    # define the fields for your item here like:
    # 拷问：需要哪些数据
    # 编号、名称、地址、城市、省份
    row_num = scrapy.Field()
    store_name = scrapy.Field()
    address_detail = scrapy.Field()
    city_name = scrapy.Field()
    province_name = scrapy.Field()

