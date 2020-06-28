# -*- coding: utf-8 -*-
import pymysql
from .settings import *
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class KfcPipeline(object):
    def process_item(self, item, spider):
        return item

class KfcMysqlPipeline(object):
    def open_spider(self,spider):
        self.db = pymysql.connect(MYSQL_HOST,MYSQL_USER,MYSQL_PWD,MYSQL_DB,charset=CHARSET)
        self.cur = self.db.cursor()

    def process_item(self,item,spider):
        ins = 'insert into kfctab values(%s,%s,%s,%s,%s)'
        li = [
            item['row_num'],
            item['store_name'],
            item['address_detail'],
            item['city_name'],
            item['province_name'],
        ]
        self.cur.execute(ins,li)
        self.db.commit()
        return item

    def close_spider(self):
        self.cur.close()
        self.db.close()
