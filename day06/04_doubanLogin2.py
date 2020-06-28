"""
模拟登录豆瓣方法2
思路：
    1.先登录成功1次，抓取到Cookie
    2.Cookie处理成字典，然后利用 requests.get()中的cookies参数
"""
import requests


def login():
    url = 'https://www.douban.com/people/214205812/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }
    # F12抓包抓到的Cookie
    cook_str = 'bid=-5scRs1TPjk; ll="118237"; _vwo_uuid_v2=D561F051CB778456C9CA56338308AD8B6|a111e66e76d32bc37cca31ab9bc0d18d; __utmc=30149280; __utmz=30149280.1587889460.3.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ses.100001.8cb4=*; __utma=30149280.352580137.1587743181.1587912559.1588062278.5; __utmt=1; dbcl2="214205812:E4lewC2IgWo"; ck=2ZcO; ap_v=0,6.0; __gads=ID=facf3e2a28ef6f7e:T=1588062308:S=ALNI_MbOUzqkFZ29PcnhIBnLwtvOf3v2qA; push_noty_num=0; push_doumail_num=0; __utmv=30149280.21420; douban-profile-remind=1; _pk_id.100001.8cb4=26745377c21b521d.1587889444.2.1588062363.1587889575.; __utmb=30149280.11.10.1588062278'
    # get_cookies(cook_str): 把字符串的cookie处理为字典
    cookies = get_cookies(cook_str)
    html = requests.get(url=url, headers=headers, cookies=cookies).text
    print(html)


def get_cookies(cook_str):
    """处理cookie为字典"""
    cookies = {}
    for kv in cook_str.split(';'):
        key = kv.split('=')[0]
        value = kv.split('=')[1]
        cookies[key] = value

    return cookies


login()
