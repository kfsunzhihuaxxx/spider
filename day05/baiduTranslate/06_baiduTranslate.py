"""
    百度翻译结果抓取
"""
import requests
import execjs
import re


class BaiduTranslateSpider:
    def __init__(self):
        self.url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
        self.headers = {
            'Cookie': 'BDUSS=21Menc5WnA3WEZIQkgwQ3c1b2Nyai1Ib1F0aVN0dnZUNXJiUXRUVmpvZWhIQkpkSVFBQUFBJCQAAAAAAAAAAAEAAAA9EtWZtPPC7brvb08AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKGP6lyhj-pcc; BAIDUID=BE8835F4F56A14DAD0C2AB3D46B5D284:FG=1; PSTM=1573989801; BIDUPSID=63184CF18B2086374D1D1F43C48F5295; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=2; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=31278_1460_31325_21079_31426_31342_30909_30823_31164; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1587898631; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1587898631; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; __yjsv5_shitong=1.0_7_0d7bf975fcd8770c26b0f0e9a88ffe77a0a1_300_1587898631852_219.157.201.113_1a82287d; yjs_js_security_passport=8e8c9811d449b8b9c38b1314770b1c8ce76dd129_1587898636_js',
            'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }

    def get_gtk_token(self):
        '''向翻译主页发送请求,正则获取gtk和token'''
        index_url = 'https://fanyi.baidu.com/#en/zh/'
        html = requests.get(url=index_url, headers=self.headers).text
        gtk = re.findall("window.gtk = '(.*?)'", html, re.S)[0]
        token = re.findall("token: '(.*?)'", html, re.S)[0]
        # print(token)
        return gtk, token

    def get_sign(self, word):
        '''获取sign - form表单中只缺少这一个数据'''
        gtk, token = self.get_gtk_token()
        with open('translate.js', 'r') as f:
            js_code = f.read()
        loader = execjs.compile(js_code)
        return loader.call('e', word, gtk)

    def translate(self, word):
        '''具体翻译函数'''
        sign = self.get_sign(word)
        gtk, token = self.get_gtk_token()
        data = {
            "from": "en",
            "to": "zh",
            "query": word,
            "transtype": "translang",
            "simple_means_flag": "3",
            "sign": sign,
            "token": token,
            "domain": "common",
        }
        html = requests.post(url=self.url, data=data, headers=self.headers).json()
        return html['trans_result']['data'][0]['dst']

    def run(self):
        word = input("请输入要翻译的单词：")
        print(self.translate(word))


if __name__ == '__main__':
    spider = BaiduTranslateSpider()
    spider.run()
