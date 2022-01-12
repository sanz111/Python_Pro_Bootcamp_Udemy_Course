Chrome_Driver_Path = "/Users/dongwei/JoeyDong/development_files/ChromeDriver/chromedriver"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

# 注：webdriver.Chrome 进行了改动，现在不能直接传 path， 要现将 path 传入 service，再传入webdriver.Chrome
service = ChromeService(executable_path=Chrome_Driver_Path)
driver = webdriver.Chrome(service=service)

# ----------------------------------- 示例 1 -----------------------------------
# 我们可以使用短短 3 行代码实现 Amazon 页面的价格抓取。因为我们是直接调用的浏览器来实现，浏览器会帮我们搞定 header 等操作，从而实现了代码的简化。而不是使用 requests.get 的方式获取 html 数据。
# 此时我们是完全模仿了一个真实的人打开浏览器，等待加载，再关闭浏览器 的一系列操作。
# driver.get("https://www.amazon.com/Fellowes-LX22M-Powershred-Shredder-5263201/dp/B07YQLPJDQ/ref=sr_1_2_sspa?keywords=amazonbasics&pd_rd_r=21430ba1-c561-43e9-b6b1-9f289f06505d&pd_rd_w=q7iTL&pd_rd_wg=kPAFq&pf_rd_p=9349ffb9-3aaa-476f-8532-6a4a5c3da3e7&pf_rd_r=T45H11M3T4HSGXKX5SWN&qid=1641796318&sr=8-2-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyVlU3WkI2R1RZWUVVJmVuY3J5cHRlZElkPUEwMjkyMDQ1MkVEMDYySkdJSENJQiZlbmNyeXB0ZWRBZElkPUEwMjQ4NzE5MkpMUE9KMTNORVc3RSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1")
# price = driver.find_element_by_id("corePrice_desktop")
# print(price.text)
#
# driver.close()  # close 实际上是关闭了一个标签，Chrome 还会停留在 mac dock 栏里面
# driver.quit()  # quit 关闭整个浏览器，不管里面有多少个标签

# ----------------------------------- 示例 2 -----------------------------------
# # 可以轻松的获取页面上的 input
# driver.get("https://www.python.org/")
# search_bar =  driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))
# # 获取 python 主页 logo 的尺寸信息
# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)
# # 获取 .documentation-widget 类里面的 a 标签
# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)
# # 当其他的获取元素的方式失效了，难以定位某个元素的时候，永远有 XPath 的方式使用。注意单双引号
# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)
# driver.quit()

# ----------------------------------- 示例 3：抽取 python 主页的 upcoming events -----------------------------------
driver.get("https://www.python.org/")
event_times = driver.find_elements_by_css_selector(".event-widget time")  # 获取 .event-widget 类里面的 time 标签
event_names = driver.find_elements_by_css_selector(".event-widget li  a")  # 获取 .event-widget 类里面的 li 标签里面的 a 标签
events = {}
for n in range(len(event_times)):
    events[n] = {
        "time":event_times[n].text,
        "name":event_names[n].text,
    }

print(events)
driver.quit()
