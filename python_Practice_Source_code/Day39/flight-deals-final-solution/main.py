from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()  # 获取 sheet 表格中的每一行数据
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

print(sheet_data)

# 如果 sheet 数据第一行的 iata code 为空，循环每一行数据并查询城市缩写代码，更新进 sheet 表格中
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

# timedelta 用于时间日期的计算
# datetime 数据不能直接计算加减法，要将待计算的数据放入 timedelta 中处理
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))


for destination in sheet_data:
    # 获取航班信息
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,  # 起飞城市代码
        destination["iataCode"],  # 目的地城市代码
        from_time=tomorrow,  # 查询起始时间：明天开始
        to_time=six_month_from_today  # 查询终止时间：六个月后
    )
    # 如果 航班价格 < sheet 表格中的最低价
    if flight.price < destination["lowestPrice"]:
        # 调用发送短信的方法
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )
