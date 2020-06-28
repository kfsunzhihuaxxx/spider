'''
输入搜索关键字，把响应内容保存到本地文件
'''
import requests
from urllib import parse


# 1.拼接url地址：http://www.baidu.com/s?wd=xxx
keyword = input("请输入关键字：")
parmas = parse.urlencode({'wd':keyword})
url = 'http://www.baidu.com/s?{}'.format(parmas)
# 2.获取响应内容
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
response = requests.get(url=url,headers=headers).text
# 3.保存到本地文件
filename = '{}.html'.format(keyword)
with open(filename,'w',encoding='utf-8') as f:
    f.write(response)