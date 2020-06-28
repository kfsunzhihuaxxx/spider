import requests
from fake_useragent import UserAgent
from lxml import etree
import time
import random

url = 'http://bj.lianjia.com/ershoufang/pg1'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
html = requests.get(url=url, headers=headers).text

p = etree.HTML(html)
li_list = p.xpath(' //ul[@class="sellListContent"]/li')
item = {}
for li in li_list:
    item['name'] = li.xpath('.//div[@class="positionInfo"]/a[1]/text()')[0].strip()
    item['address'] = li.xpath('.//div[@class="positionInfo"]/a[2]/text()')[0].strip()
    info_list = li.xpath('.//div[@class="houseInfo"]/text()')[0].split('|')
    item['model'] = info_list[0]
    item['area'] = info_list[1]
    item['direct'] = info_list[2]
    item['perfect'] = info_list[3]
    item['floor'] = info_list[4]
    item['year'] = info_list[5]
    item['type'] = info_list[6]
    item['total'] = li.xpath('.//div[@class="totalPrice"]/span/text()')[0].strip()
    item['unit'] = li.xpath('.//div[@class="unitPrice"]/span/text()')[0].strip()
    print(item)
