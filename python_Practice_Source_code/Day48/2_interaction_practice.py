# 本 demo 用于演示以下功能：
#   1. 获取 wiki 主页元素
#   2. 模拟点击动作
#   3. 获取输入框，输入 "Python"，模拟回车键

Chrome_Driver_Path = "/Users/dongwei/JoeyDong/development_files/ChromeDriver/chromedriver"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys  # 用于模拟键盘输入

service = ChromeService(executable_path=Chrome_Driver_Path)
driver = webdriver.Chrome(service = service)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element_by_css_selector("#articlecount a")
print(article_count.text)
# article_count.click()  # 点击选中的这个元素

all_portals = driver.find_element_by_link_text("All portals")  # 查找链接名称为 "All portals"的链接元素
# all_portals.click()

search = driver.find_element_by_name("search")  # 获取输入框元素
search.send_keys("Python")  # 在输入框中输入 "Python"
search.send_keys(Keys.ENTER)  # 在输入框中按回车
driver.quit()