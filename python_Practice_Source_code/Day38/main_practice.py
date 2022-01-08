import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 60
HEIGHT_CM = 174
AGE = 30

APP_ID = "ae4c78f1"
API_KEY = "8e09133662b9421098b0f0d86f4e03ff"

exercise_point = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/aef4dd4f246f11abcf72d3dfc8fa7f19/workoutTracking/workouts"

exercise_text = input("Tell me which exercises you did:")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query" : exercise_text,
    "gender": GENDER,
    "weight_kg" : WEIGHT_KG,
    "height_cm" : HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_point, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

print(today_date)
print(now_time)

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout" : {
            "date":today_date,
            "time":now_time,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint,json=sheet_inputs)
    sheet_result = sheet_response.json()
    print(sheet_result)
