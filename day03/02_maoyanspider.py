"""
猫眼电影top100抓取（电影名称、主演、上映时间）
存入csv文件 使用writerow()方法
"""

import requests
import re
import time
from lxml import etree
import random

class MaoyanSpider:
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
        #打开文件,并初始化写入对象

    def get_html(self, url):
        html = requests.get(url=url, headers=self.headers).text
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        """解析提取数据"""
        p = etree.HTML(html)
        # 基准的xpath： 每个电影信息的对象dd列表[<element dd at xxx>,<element dd at xx1>,...]
        dd_list = p.xpath('//dl[@class="board-wrapper"]/dd')
        item = {}
        for dd in dd_list:
            item['name'] = dd.xpath('.//p[@class="name"]/a/@title')[0].strip()
            item['star'] = dd.xpath('.//p[@class="star"]/text()')[0].strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()')[0].strip()
            print(item)


    def save_html(self, r_list):
        pass

    def run(self):
        """程序入口函数"""
        for offset in range(0, 4, 10):
            url = self.url.format(offset)
            self.get_html(url=url)
            # 控制数据抓取频率:uniform()生成指定范围内的浮点数
            time.sleep(random.uniform(0,1))




if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()










