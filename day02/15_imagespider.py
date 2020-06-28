'''抓取图片到本地'''


import requests
url = 'https://timgsa.baidu.com/timg?'
headers = {"User-Agent":"Mozilla/5.0"}


html = requests.get(url=url,headers=headers).content
with open("萤火虫.jpg",'wb') as f:
    f.write(html)