"""
猫眼电影top100抓取（电影名称、主演、上映时间）
"""
import pymysql
import requests
import re
import time
import random

class MaoyanSpider:
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
        self.db = pymysql.connect('localhost','root','123456','maoyandb',charset='utf8')
        self.cur = self.db.cursor()

    def get_html(self, url):
        html = requests.get(url=url, headers=self.headers).text
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        """解析提取数据"""
        regex = '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>'
        pattern = re.compile(regex, re.S)
        r_list = pattern.findall(html)
        # r_list: [('活着','牛犇','2000-01-01'),(),(),...,()]
        self.save_html(r_list)

    def save_html(self, r_list):
        """数据处理函数"""
        ins = "insert into maoyantab values(%s,%s,%s)"
        for r in r_list:
            li = [r[0].strip(),r[1].strip(),r[2].strip()]
            self.cur.execute(ins,li)
            #千万别忘记提交到数据库
            self.db.commit()
            print(li)

    def run(self):
        """程序入口函数"""
        for offset in range(0, 91, 10):
            url = self.url.format(offset)
            self.get_html(url=url)
            # 控制数据抓取频率:uniform()生成指定范围内的浮点数
            time.sleep(random.uniform(1,2))
            self.cur.close()
            self.db.close()

if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()










