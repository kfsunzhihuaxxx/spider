'''
json.dump()
使用场景：
    把抓取的数据保存到本地json文件中
'''

import json

all_file_list = [
    {'rank':'1','name':'霸王别姬','star':'张国荣'},
    {'rank':'2','name':'大话西游','star':'周星驰'}

]
# 保存到file.json文件中
with open('film.json','w') as f:
    json.dump(all_file_list,f,ensure_ascii=False)