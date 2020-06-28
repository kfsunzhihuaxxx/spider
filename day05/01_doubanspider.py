'''
豆瓣电影数据提取 抓取剧情类别下的所有电影
'''
import json
import time

import requests
import random
from fake_useragent import UserAgent


class DoubanSpider:
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start={}&limit=20'

    def get_html(self, url):
        '''功能函数1 请求函数'''
        headers = {"User-Agent": UserAgent().random}
        html = requests.get(url=url, headers=headers).text
        return html

    def parse_html(self, url):
        '''提取电影信息的函数'''
        html = json.loads(self.get_html(url=url))
        print(html)
        item = {}
        for one_film in html:
            item['rank'] = one_film['rank']
            item['name'] = one_film['title']
            item['time'] = one_film['release_date']
            item['score'] = one_film['score']
            print(item)

    def run(self):
        '''程序入口函数'''
        # 获取某个类别下的电影的总数量
        total = self.get_total()
        for start in range(0, total, 20):
            url = self.url.format(start)
            self.parse_html(url=url)
            time.sleep(random.randint(1, 2))

    def get_total(self):
        '''获取某个类别下的电影的总数量'''
        page_url = 'https://movie.douban.com/j/chart/top_list_count?type=11&interval_id=100%3A90'
        html = json.loads(self.get_html(url=page_url))
        total = html['total']
        return total

    

if __name__ == '__main__':
    spider = DoubanSpider()
    spider.run()
