'''打开浏览器打开百度停留在页面'''


#导入webdriver借口

from selenium import webdriver


# 1打开浏览器 - 创建浏览器对象
driver = webdriver.Chrome()

# 2输入url地址
driver.get('http://www.baidu.com/')

# 3获取屏幕截图
driver.save_screenshot('baidu.png')

print(driver.page_source.find('pn-next disabled'))