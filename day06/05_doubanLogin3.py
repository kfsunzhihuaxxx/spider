'''
思路：
    1.实例化session对象
    2.登录网站 -s.post()
    3.抓取数据 -s.get()
'''

import requests

s = requests.session()

def login():
    # 1 登录
    post_url = 'https://accounts.douban.com/j/mobile/login/basic'
    data = {
        'ck' : '',
        'name' : '18911782528',
        'password' : 'Aiya239239',
        'remeber' : 'false',
        'ticket' : '',
    }
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Cookie':'bid=-5scRs1TPjk; ll="118237"; _vwo_uuid_v2=D561F051CB778456C9CA56338308AD8B6|a111e66e76d32bc37cca31ab9bc0d18d; apiKey=; __utmc=30149280; __utmz=30149280.1587889460.3.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; login_start_time=1588062288317; last_login_way=account; ap_v=0,6.0; __gads=ID=facf3e2a28ef6f7e:T=1588062308:S=ALNI_MbOUzqkFZ29PcnhIBnLwtvOf3v2qA; push_noty_num=0; push_doumail_num=0; __utmv=30149280.21420; douban-profile-remind=1; __utma=30149280.352580137.1587743181.1588062278.1588065028.6; _pk_ref.100001.2fad=%5B%22%22%2C%22%22%2C1588067601%2C%22https%3A%2F%2Fwww.douban.com%2Fpeople%2F214205812%2F%22%5D; _pk_ses.100001.2fad=*; _pk_id.100001.2fad=c3c9bb05c2e27054.1588067601.1.1588068550.1588067601.'
    }
    s.post(url=post_url,data=data,headers=headers)
    #2 抓取具体数据
    get_url = 'https://www.douban.com/people/214205812/'
    get_headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    html = s.get(url=get_url,headers=get_headers).text
    print(html)




login()