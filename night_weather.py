import requests
import json
import os
from utils.weather_utils import log

LAT = os.environ["LAT"]
LON = os.environ["LON"]
OWM_API_KEY = os.environ["OWM_API_KEY"]

# Get current weather
url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&units=metric&appid={OWM_API_KEY}"
data = requests.get(url).json()

log(f"OWM night weather fetched: {data}")

# Extract night weather
night_data = {
    "temp": data["main"]["temp"],
    "feels_like": data["main"]["feels_like"],
    "temp_min": data["main"]["temp_min"],
    "temp_max": data["main"]["temp_max"],
    "humidity": data["main"]["humidity"],
    "pressure": data["main"]["pressure"],
    "wind_speed": data["wind"]["speed"],
    "wind_deg": data["wind"]["deg"],
    "weather_desc": data["weather"][0]["description"],
    "clouds": data["clouds"]["all"],
    "visibility": data.get("visibility", "N/A"),
}

with open("night_weather.json", "w") as f:
    json.dump(night_data, f)
log("Night artifact created: night_weather.json")