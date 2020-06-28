# -*- coding: utf-8 -*-
import pymysql
from .settings import *
import pymongo


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 管道1 终端打印输出
class GuaziPipeline(object):
    def process_item(self, item, spider):
        print(item['name'],item['link'],item['price'])
        return item


# 管道2 存入mysql 数据库
class GuaziMysqlPipeline(object):
    def open_spider(self,spider):
        '''在爬虫项目启动时，只执行一次，一般用于数据库的链接'''
        self.db = pymysql.connect(MYSQL_HOST,MYSQL_USER,MYSQL_PWD,MYSQL_DB,charset=CHARSET)
        self.cur = self.db.cursor()


    def process_item(self, item, spider):
        ins = 'insert into cartab values(%s,%s,%s)'
        li = [
            item['name'],item['price'],item['link']
        ]
        self.cur.execute(ins,li)
        self.db.commit()
        return item


    def close_spider(self,spider):
        '''在爬虫程序结束时，只执行一次一般用于数据库的断开'''
        self.cur.close()
        self.db.close()

# 管道3  存入mongo 数据库
class GuaziMongoPipeline(object):
    def open_spider(self,spider):
        '''在爬虫项目启动时，只执行一次，一般用于数据库的链接'''
        self.conn = pymongo.MongoClient(MONGO_HOST,MONGO_PORT)
        self.db = self.conn[MONGO_DB]
        self.myset = self.db[MONGO_SET]

    def process_item(self, item, spider):
        self.myset.insert_one(dict(item))
        return item


