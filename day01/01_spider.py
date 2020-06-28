'''
京东首页spider
'''
import requests


# 1.get()方法得到的为相应对象 而不是内容
response = requests.get(url='http://www.jd.com/')
# 2.text属性：获取响应内容（字符串）
html = response.text
# 3.content属性：获取响应内容（bytes类型）-图片/音频/视频/文件...
html = response.content
# 4.status_code:HTTP响应码
code = response.status_code
# 5.url：实际返回数据的url地址
url = response.url
print(url)