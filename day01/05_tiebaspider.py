'''
百度贴吧spider
'''
# 1.请输入贴吧名：
# 2.请输入起始页：
# 3.请输入终止页：
# 最终保存：xxx吧＿第X页.html　... ...
import requests
from urllib import parse
import random
import time


class TiebaSpider:
    def __init__(self):
        '''定义常用变量'''
        self.url = 'http://tieba.baidu.com/f?kw={}&pn={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
        }

    def get_html(self, url):
        '''请求功能函数－获取html'''
        html = requests.get(url=url, headers=self.headers).text
        return html

    def parse_html(self):
        '''解析功能函数－数据解析提取'''
        pass

    def save_html(self, filename, html):
        '''数据处理功能函数－数据的存储'''
        with open(filename, 'w') as f:
            f.write(html)

    def run(self):
        '''程序的入口函数－整个程序的逻辑调用'''
        name = input("请输入贴吧名：")
        start = int(input('请输入起始页：'))
        end = int(input('请输入终止页：'))
        #编码
        params = parse.quote(name)
        for page in range(start,end+1):
            pn = (page-1)*50
            url = self.url.format(params,pn)
            #请求　+　保存
            html = self.get_html(url=url)
            filename='{}_第{}页.html'.format(name,page)
            self.save_html(filename,html)
            # 控制一下爬取频率
            time.sleep(random.uniform(1,2))
            print("第{}页爬取完成".format(page))


if __name__ == '__main__':
    spider = TiebaSpider()
    spider.run()
