import requests

# ---------------------------- Demo1：国际空间站运行位置 API 使用示例 ------------------------------- #
# API 的简易使用方法
# 国际空间站当前运行位置api页面： http://open-notify.org/Open-Notify-API/ISS-Location-Now/
# 能够获取当前经纬度信息

# response =  requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
# response.raise_for_status()
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude,latitude)
#
# print(iss_position)


# ---------------------------- Demo2：日出日落 API 使用示例 ------------------------------- #
# 经纬度查询网址： https://www.latlong.net/
# 从上述网址可得，京都的经纬度为： Latitude:35.011635, Longitude:135.768036
from datetime import datetime
MY_LAT = 35.011635
MY_LONG = 135.768036
parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0
}

response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()
print(data)
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunset_hour = sunset.split("T")[1].split(":")[0]
print(sunrise_hour)
print(sunset_hour)

time_now_hour = datetime.now().hour
print(time_now_hour)
