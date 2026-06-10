import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_weather(city):
    """
    Fetch current weather for a city.
    """

    try:
        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}"
            f"&appid={API_KEY}"
            f"&units=metric"
        )

        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            return None

        weather_data = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"].title(),
            "wind_speed": data["wind"]["speed"]
        }

        return weather_data

    except Exception as e:
        print(f"Weather Error: {e}")
        return None