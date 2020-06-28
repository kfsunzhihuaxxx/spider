"""
抓取有道翻译的翻译结果
思路：
    # 1 翻译的结果为动态加载，F12开始抓包
    # 2 页面中翻译单词，在XHR中找到具体的网络数据包
    # 3 分析数据包
        3.1)Request URL: POST的URL地址
        3.2)Request Headers:请求头
        3.3)Request Data: Form表单数据
    # 4 html = request.post(url=url,data=data,headers=headers).text
"""
import requests
import time
import random
from hashlib import md5

class YdSpider:
    def __init__(self):
        # url为F12抓包抓到的URL地址(POST)
        self.url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.headers = {
"Accept": "application/json, text/javascript, */*; q=0.01",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9",
"Connection": "keep-alive",
"Content-Length": "244",
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"Cookie": "OUTFOX_SEARCH_USER_ID=-737795482@10.108.160.105; JSESSIONID=aaaMxlFw6vrAZ-hkx7Qgx; OUTFOX_SEARCH_USER_ID_NCOO=1338048684.529694; ___rl__test__cookies=1587738342774",
"Host": "fanyi.youdao.com",
"Origin": "http://fanyi.youdao.com",
"Referer": "http://fanyi.youdao.com/",
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
"X-Requested-With": "XMLHttpRequest",
}

    def get_ts_salt_sign(self,word):
        '''功能函数：获取到ts,salt,sign用来完善form表单数据'''
        ts = str(int(time.time()*1000))
        salt = ts + str(random.randint(0,9))
        s = md5()
        # md5("fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj")
        string = 'fanyideskweb'+word+salt+'Nw(nmmbP%A-r6U3EUn]Aj'
        s.update(string.encode())
        sign = s.hexdigest()
        return ts,salt,sign

    def get_result(self,word):
        #获取ts,salt,sign
        ts,salt,sign = self.get_ts_salt_sign(word)
        data = {
        "i": word,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": sign,
        "ts": ts,
        "bv": "94ef9c063d6b2a801fab916722d70203",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_CLICKBUTTION",
        }
        # .json():直接获取python数据类型,前提事网站返回的数据必须为json类型
        html = requests.post(url=self.url,data=data,headers=self.headers).json()
        result = html['translateResult'][0][0]['tgt']
        return result



    def run(self):
        word = input("请输入要翻译的单词：")
        print(self.get_result(word))


if __name__ == '__main__':
    spider = YdSpider()
    spider.run()