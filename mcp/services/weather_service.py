import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(city):

    api_key = os.getenv("WEATHER_API_KEY")

    print("City:", city)
    print("API Key:", api_key)

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    print("Status Code:", response.status_code)
    print("Response:", response.text)

    data = response.json()

    if response.status_code != 200:
        return {
            "error": data.get("message", "Unknown error")
        }

    return {
        "temp": data["main"]["temp"],
        "condition": data["weather"][0]["description"]
    }