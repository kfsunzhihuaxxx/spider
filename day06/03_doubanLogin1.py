"""
抓取我的豆瓣主页--需要登录才能访问的页面
思路：
    1.先登录成功，F12抓取到对应的Cookie
    2.利用requests.get()中的 headers参数
"""

import requests



def login():
    url = 'https://www.douban.com/people/214205812/'
    headers = {
        'Cookie':'ll="108288"; bid=EzMxcUbfY28; _vwo_uuid_v2=D43990B53186CB5D5D281786329F6B7D0|7590379b31aa416216ff9c72b7aea02c; douban-fav-remind=1; __gads=ID=c82e3cfbdeb64e0b:T=1580992622:S=ALNI_MbkXpx-2yO3NishTmaCCV3Xm602MQ; __yadk_uid=mvgQzCASSvvyubXs7dHh2X7g00Cf6Ekh; ap_v=0,6.0; __utmc=30149280; __utmz=30149280.1587956473.7.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; dbcl2="214205812:E4lewC2IgWo"; ck=2ZcO; push_noty_num=0; push_doumail_num=0; __utma=30149280.858813859.1558924114.1587956473.1587958526.8; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1587958722%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D-u2mgJ8J1m8pBs1vcrSodmTa9M8PSvJvMTHGkryneKzC7aEqosZM7uaIBTEEkURX%26wd%3D%26eqid%3Db40e321e00020ef5000000025ea653bd%22%5D; _pk_ses.100001.8cb4=*; __utmt=1; __utmv=30149280.21420; douban-profile-remind=1; _pk_id.100001.8cb4=6b93af9647feea9c.1580992623.2.1587958844.1580992623.; __utmb=30149280.6.10.1587958526',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }
    html = requests.get(url=url,headers=headers).text
    # 最终在html中确认：是否存在个人主页的一些数据
    print(html)

login()