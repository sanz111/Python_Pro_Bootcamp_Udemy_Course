import requests
from datetime import datetime,timedelta

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/aef4dd4f246f11abcf72d3dfc8fa7f19/flightDeals/prices"
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "8ZZgaLf8HwJBjLi-ydWRuFIkUvw6FHy0"
ORIGIN_CITY_IATA = "LON"

# Part 1：获取 sheet 表格中的数据
response = requests.get(url=SHEETY_PRICES_ENDPOINT)
data = response.json()
# 取出 sheet 表中每一行的值
destination_data = data["prices"]
# print(destination_data)
#
# for city_row_data in destination_data:
#     print(city_row_data)
#     new_data = {
#         "price":{
#             "iataCode" : "KIX"
#         }
#     }
#     response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city_row_data['id']}", json= new_data)

# Part 2：查询目的地代码
# location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
# headers = {"apikey": TEQUILA_API_KEY}
# query = {"term": "Paris", "location_types": "city"}
# response = requests.get(url=location_endpoint, headers=headers, params=query)
# results = response.json()["locations"]
# code = results[0]["code"]
# print(code)

# Part 3：
print(destination_data[0])
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_tomorrow = datetime.now() + timedelta(days=180)

headers = {"apikey": TEQUILA_API_KEY}
query = {
            "fly_from": ORIGIN_CITY_IATA,
            "fly_to": destination_data[0]["iataCode"],
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": six_month_from_tomorrow.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",  # 往返
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"  # 货币代码
        }
response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )
data = response.json()["data"][0]
print(data)

flight_data = {
    "price" : data["price"],
    "origin_city":data["route"][0]["cityFrom"],
    "origin_airport":data["route"][0]["flyFrom"],
    "destination_city":data["route"][0]["cityTo"],
    "destination_airport":data["route"][0]["flyTo"],
    "out_date":data["route"][0]["local_departure"].split("T")[0],
    "return_date":data["route"][1]["local_departure"].split("T")[0]
}
print(flight_data)