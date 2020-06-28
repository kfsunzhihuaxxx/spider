# -*- coding: utf-8 -*-
import json

import requests
import scrapy
from urllib import parse
from ..items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['careers.tencent.com']
    one_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1566266592644&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
    two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1566266695175&postId={}&language=zh-cn'
    keyword = input("请输入职位类别")
    params = parse.quote(keyword)
    # start_urls:keyword 类别下的第1页的URL地址
    start_urls = [one_url.format(params,1)]

    def parse(self, response):
        '''生成所有的一级页面url地址，交给调度器入队列'''
        total = self.get_total()
        for page in range(1,total+1):
            url = self.one_url.format(self.params,page)
            # dont_filter:交给调度器的请求不参与去重
            yield scrapy.Request(url=url,callback=self.parse_one_page,dont_filter=True)

    def get_total(self):
        '''获取总页数'''
        url = self.one_url.format(self.params, 1)
        html = requests.get(url=url,headers={
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        }).json()
        cou = html['Data']['Count']
        total = cou // 10 if cou % 10 == 0 else cou // 10 + 1

        return total

    def parse_one_page(self,response):
        '''一级页面解析函数：提取postid,拼接二级页面URL地址，交给调度器入队列'''
        html = json.loads(response.text)
        for one_job in html['Data']['Posts']:
            post_id = one_job['PostId']
            # 每页拼接10个职位的详情页链接
            two_url = self.two_url.format(post_id)
            yield scrapy.Request(url=two_url, callback=self.parse_two_page,dont_filter=True)

    def parse_two_page(self,response):
        '''二级页面解析函数：提取每个职位的具体数据'''
        two_html = json.loads(response.text)
        item = TencentItem()
        item['job_name'] = two_html['Data']['RecruitPostName']
        item['job_address'] = two_html['Data']['LocationName']
        item['job_type'] = two_html['Data']['CategoryName']
        item['job_duty'] = two_html['Data']['Responsibility']
        item['job_require'] = two_html['Data']['Requirement']
        item['job_time'] = two_html['Data']['LastUpdateTime']
        yield item