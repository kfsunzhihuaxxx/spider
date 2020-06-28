'''
qq邮箱登录
'''
from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://mail.qq.com/')

# 第一种切换iframe方式
# node_iframe =driver.find_elements_by_xpath('//*[@id="login_frame"]')
# driver.switch_to.frame(node_iframe)
# 第二种切换iframe方式
driver.switch_to.frame("login_frame")  #driver.switch_to.frame(class="login_frame")
#switch_to.frame()参数为id或者class的属性值

driver.find_element_by_id('u').send_keys('594942776@qq.com')
driver.find_element_by_id('p').send_keys('Aiya239239')
driver.find_element_by_xpath('//*[@id="login_button"]').click()

driver.find_element_by_class_name('btn.btn-account').click()