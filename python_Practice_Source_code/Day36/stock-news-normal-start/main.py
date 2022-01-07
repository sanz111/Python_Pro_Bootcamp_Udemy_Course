STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "XD34DFZY5LLKS8VP"
NEWS_API_KEY = "99e8fb07a9184ccdbecec9d86020615b"
TWILIO_SID = "ACe966a446589694915af53f604a835fab"
TWILIO_AUTH_TOKEN = "e7c7c342fec6a85be955b5694fb80884"

import requests
from twilio.rest import Client

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, stock_params)
response.raise_for_status()
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_data = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_data)

difference = float(day_before_yesterday_closing_data) - float(yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "⤴"
else:
    up_down = "⤵"
print(difference)

diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)

if abs(diff_percent) > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)

    formatted_articles = [
        f"{STOCK_NAME}:{up_down} {diff_percent}%\nHeadline: {article['title']}.\nBrief: {article['description']}." for
        article in
        three_articles]
    print(formatted_articles)
    # Send each article as a separate message via Twilio.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='+12672147361',
            to='+818046419568'
        )
        print(message.sid)
