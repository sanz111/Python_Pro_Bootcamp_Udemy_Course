import requests
from twilio.rest import Client

api_key = "f8d3e62ee9753b26acfd3380fac7f331"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

account_sid = "ACe966a446589694915af53f604a835fab"
auth_token = "4010544a1522c90a118ab013f1a29883"

weather_parameters = {
    "lat": 35.011635,
    "lon": 135.768036,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint,params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code)< 800:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_='+12672147361',
        to='+818046419568'
    )
    print(message.sid)
