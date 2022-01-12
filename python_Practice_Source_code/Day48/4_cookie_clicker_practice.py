Chrome_Driver_Path = "/Users/dongwei/JoeyDong/development_files/ChromeDriver/chromedriver"

from selenium import webdriver
import time

driver = webdriver.Chrome(Chrome_Driver_Path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# 获取 cookie 元素
cookie = driver.find_element_by_id("cookie")

# 获取右侧按钮面板的8个按钮
items = driver.find_elements_by_css_selector("#store div")  # id=store 下面的 div 元素
item_ids = [item.get_attribute("id") for item in items]  # 获取 id 值

print(item_ids)

# 备注：time.time() 返回当前时间的时间戳（1970纪元后经过的浮点秒数
timeout = time.time() + 5  # 加 5s
five_min = time.time() + 60  # 加 5 minutes

all_prices = driver.find_elements_by_css_selector("#store b")
item_prices = []


while True:
    cookie.click()

    # 每 5s
    if time.time() > timeout:
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                # 对文本进行整理：以 "-" 分割，去除空格，去除千分号","，转为整形变量
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # 创建字典存储 items 和 prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            # 将上述抽取到的 id 值 与 price 值对应，格式类似于：
            # {15:'buyCursor, 100:'buyGrandma' }
            cookie_upgrades[item_prices[n]] = item_ids[n]
        print(cookie_upgrades)

        # 获取当前的 cookie 数量值
        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",","")
        cookie_count = int(money_element)

        # 找出我们当前可以支付支付的起的元素
        affordable_upgrades = {}
        for cost,id in cookie_upgrades.items():  # 注意循环字典内的值的格式
            if cookie_count > cost:  # 当 cookie 数值大于 price 的时候，将 cost 和 id 保存进字典
                affordable_upgrades[cost] = id

        # 买最贵的那个
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)  # 找出能买的起的最贵的那个值
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]  # 找到对应的 id 值
        driver.find_element_by_id(to_purchase_id).click()  # 按照 id 值找到页面的元素，点击

        # 当前时间点 +5s
        timeout = time.time() +5

        # 当运行时间超过5分钟时，停止运行，并从页面中读取 cookie per second 值
        if time.time() > five_min:
            cookie_per_s = driver.find_element_by_id("cps").text
            print(cookie_per_s)
            break
