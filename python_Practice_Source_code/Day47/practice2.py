# 以 practice1 为准
# 这个文件仅用来测试

import requests
from bs4 import BeautifulSoup


BUY_PRICE = 10000
MY_EMAIL= "jackma22336677@gmail.com"
MY_PASSWORD = "4$dbxxr#i!HtN3G9"


url = "https://www.amazon.com/Fellowes-LX22M-Powershred-Shredder-5263201/dp/B07YQLPJDQ/ref=sr_1_2_sspa?keywords=amazonbasics&pd_rd_r=21430ba1-c561-43e9-b6b1-9f289f06505d&pd_rd_w=q7iTL&pd_rd_wg=kPAFq&pf_rd_p=9349ffb9-3aaa-476f-8532-6a4a5c3da3e7&pf_rd_r=T45H11M3T4HSGXKX5SWN&qid=1641796318&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyVlU3WkI2R1RZWUVVJmVuY3J5cHRlZElkPUEwMjkyMDQ1MkVEMDYySkdJSENJQiZlbmNyeXB0ZWRBZElkPUEwMjQ4NzE5MkpMUE9KMTNORVc3RSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

header = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "ccept-Language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.text, "lxml")
print(soup.prettify())

price_with_currency = soup.find(class_ = "a-offscreen").get_text()
price_without_currency = price_with_currency.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

import smtplib

title = soup.find(id="productTitle").get_text().strip()
print(title)

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price_with_currency}"

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )