# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    star = scrapy.Field()
    time = scrapy.Field()

    # 行驶里程，排量，变速箱
    km = scrapy.Field()
    displace = scrapy.Field()
    typ = scrapy.Field()
