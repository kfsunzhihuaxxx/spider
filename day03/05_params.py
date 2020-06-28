''':param参数使用'''


import requests


url = 'http://tieba.baidu.com/f?'
params = {'wd':'赵丽颖','pn':'50'}
headers = {
    "User-Agent":'Mozilla/5.0'
}
res = requests.get(url=url,params=params,headers=headers).content.decode('utf-8','ignore')
