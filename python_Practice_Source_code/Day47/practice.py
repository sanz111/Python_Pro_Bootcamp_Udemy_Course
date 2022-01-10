# 本例子用于查询 amazon 某物品的价格，当价格低于设定值时，向邮箱中发送通知邮件

# 备注：当使用日本亚马逊的链接时候，会报一个错误。这个错误跟当前环境所使用的编码格式相关。原因是日文的 "￥" python 不认。具体解决方案没有深入研究。使用美国亚马逊的"$"符号没有问题

import requests
import lxml
from bs4 import BeautifulSoup

MY_EMAIL = "jackma22336677@gmail.com"
MY_PASSWORD = "4$dbxxr#i!HtN3G9"

# 要检测的 amazon 物品链接
url = "https://www.amazon.com/Donerton-Over-Ear-Headphones-Canceling-Compatible/dp/B08JYW73G1/ref=sr_1_1_sspa?keywords=gaming+headsets&pd_rd_r=5a9ffb87-1bf3-4cca-b383-0a3166abdf89&pd_rd_w=gSfpb&pd_rd_wg=G6sLo&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=BH9M00EM95K2HYA6WH88&qid=1641794072&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzMEdZR1paNE9DQTlUJmVuY3J5cHRlZElkPUEwNjIzMDg1Mk5QV0NFWkFUSEswOSZlbmNyeXB0ZWRBZElkPUEwOTAzMTM4Mk1LWUpBNTFFR0MyTSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

# MyHttpHeader 数据。
#可以通过这个网站查询：http://myhttpheader.com/
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get(url, headers=header)

# 注意：此处一定要使用 lxml 的方式来解析 html 数据
soup = BeautifulSoup(response.text, "lxml")
print(soup.prettify())  # prettify() 函数用于格式化代码（具体功能不明）

# 获取价格数据。 class 的名称会随着网页的更新而变化，如果爬失败了可以重新去浏览器里面查一下价格标签的 class 叫什么名字
price = soup.find(class_="a-offscreen").get_text()
print(price) # 此时的价格中带有 $ 符号
price_without_currency = price.split("$")[1] # 获取价格
price_as_float = float(price_without_currency)  # 转换为浮点数
print(price_as_float)


import smtplib

# Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
title = soup.find(id="productTitle").get_text().strip()  # 获取商品名称
print(title)

BUY_PRICE = 200  # 设定购买价格，如果实际查询的价格低于购买价格，就会出发邮件通知

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )