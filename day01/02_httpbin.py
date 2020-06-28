"""
向测试网站：http://httpbin.org/get发出请求，确认请求头中的User-Agent
"""
import requests

url = 'http://httpbin.org/get'
html = requests.get(url=url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}).text
print(html)