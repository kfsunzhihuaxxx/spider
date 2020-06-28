'''
收费代理：
    建立开放代理的代理ip池
思路：
    1 现获取到开放代理
    2 依次对每个代理IP进行测试，能用的保存到文件中
'''
import requests


class ProxyPool:
    def __init__(self):
        self.url = "http://dps.kdlapi.com/api/getdps/?orderid=948769263775384&num=20&pt=1&sep=1"
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.f = open('proxy.txt','w')

    def get_html(self):
        html = requests.get(url=self.url,headers=self.headers).text
        proxy_list = html.split('\r\n')
        print(proxy_list)
        for proxy in proxy_list:
            # 依次测试每个代理IP是否可用
            if self.check_proxy(proxy):
                self.f.write(proxy+'\n')

    def check_proxy(self,proxy):
        '''测试1个代理ip是否可用,可用返回True,否则返回False'''
        test_url = 'http://httpibin.org/get'
        proxies = {
            'http':'http://{}'.format(proxy),
            'https':'https://{}'.format(proxy)
        }
        try:
            res = requests.get(url=test_url,proxies=proxies,headers=self.headers,timeout=3)
            if res.status_code == 200:
                print(proxy,'可用')
                return True
            else:
                print(proxy,'不可用')
                return False
        except Exception as e:
            print(proxy,'无效')
            return False

    def run(self):
        self.get_html()


if __name__ == '__main__':
    spider = ProxyPool()
    spider.run()