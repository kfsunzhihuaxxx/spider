# -*- coding: utf-8 -*-
import pymysql
import pymongo
from .settings import *

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MaoyanMysqlPipeline(object):
    def open_spider(self):
        self.db = pymysql.connect(MYSQL_HOST,MYSQL_USER,MYSQL_PWD,MYSQL_DB,charset=CHARSET)
        self.cur = self.db.cursor()


    def process_item(self, item, spider):
        info = [item['name'],item['star'],item['time']]
        ins = 'insert into values(%s,%s,%s)'
        self.cur.execute(ins,info)
        self.db.commit()
        return item

    def close_spider(self):
        self.cur.close()
        self.db.close()



class MaoyanMongoPipeline(object):
    def open_spider(self):
        self.conn = pymongo.MongoClient(MONGO_HOST,MONGO_PORT)
        self.db = self.conn[MONGO_DB]
        self.myset = self.db[MONGO_SET]


    def process_item(self, item, spider):
        self.myset.insert_one(dict(item))
        return item



