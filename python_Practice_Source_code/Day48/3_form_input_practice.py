# 本 demo 用于演示以下功能：
#   1. 在测试用的网页中获取 input 元素
#   2. 输入框中填入值
#   3. 模拟点击按钮，提交

# 测试用网页为： http://secure-retreat-92358.herokuapp.com/

Chrome_Driver_Path = "/Users/dongwei/JoeyDong/development_files/ChromeDriver/chromedriver"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys

service = ChromeService(executable_path=Chrome_Driver_Path)
driver = webdriver.Chrome(service=service)

driver.get("http://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element_by_name("fName")
f_name.send_keys("234")
l_name = driver.find_element_by_name("lName")
l_name.send_keys("456")
email = driver.find_element_by_name("email")
email.send_keys("123@123.com")
# submit_btn = driver.find_element_by_tag_name("button")

submit_btn = driver.find_element_by_css_selector("form button")
submit_btn.click()