# _*_ coding : utf-8 _*_
# @Time : 2022/11/29 下午 8:56
# @Author : xialijuan
# @File : auto_sign_in
# @Project : AutoSignIn
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')

path = r'C:\\Program Files\\Google\\Chrome\Application\\chrome.exe'
chrome_options.binary_location = path

browser = webdriver.Chrome(chrome_options=chrome_options)


url = 'https://purefast.net/auth/login'
browser.get(url)
print('访问网页成功!')

time.sleep(7)

email_input = browser.find_element(By.XPATH, '//input[@id="email"]')
email_input.send_keys('jake123@gmail.com')

pwd_input = browser.find_element(By.XPATH, '//input[@id="password"]')
pwd_input.send_keys('sdfoe8x983.9e')


login_btn = browser.find_element(By.XPATH, '//button[@class="btn btn-primary btn-lg btn-icon icon-right login"]')
login_btn.click()

# time.sleep(4)

# already_read_btn = browser.find_element(By.XPATH, '//button[@class="btn btn-primary"]')
# already_read_btn = browser.find_element(By.XPATH, '//body')
# already_read_btn.click()
print('成功登录')


# 获取到期时间    这里注意find_element和find_elements区别
# diminish_time_span = browser.find_elements(By.XPATH, '//span[@class="counter"]')[0]
# diminish_time =ttdiminish_time_span.text
text_h2 = browser.find_element(By.XPATH, '//div[@id="checkin-div"]//h2')
if text_h2.text == '您已签到':
    print('还没到期呢！')
else:
    # sign_in = browser.find_element(By.XPATH, '//div[@id="checkin-div"]')
    # sign_in.click()
    print('准备签到了')


input('按任意键退出')

