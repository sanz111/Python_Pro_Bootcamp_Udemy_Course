from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/aef4dd4f246f11abcf72d3dfc8fa7f19/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/aef4dd4f246f11abcf72d3dfc8fa7f19/flightDeals/users"

# DataManager 模块：
#   功能1： 获取 sheet 表格数据
#   功能2： 更新 sheet 表格中的 IATA Code 数据
class DataManager:

    def __init__(self):
        # 目的地信息清空
        self.destination_data = {}

    # 获取 sheet 表格中的数据
    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    # 用于更新 IATA Code 一列，将IATA Code 补充进表格中
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        customer_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(url=customer_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data

