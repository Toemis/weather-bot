import requests
import json
from datetime import datetime
import os

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
OWM_API_KEY = os.environ["OWM_API_KEY"]

LAT = os.environ["LAT"]
LON = os.environ["LON"]

# Load night weather
night_file = "night_weather.json"

if os.path.exists(night_file):
    with open(night_file) as f:
        night = json.load(f)
else:
    # If no file exists yet, provide default values
    night = {
        "temp": "N/A",
        "feels_like": "N/A",
        "temp_min": "N/A",
        "temp_max": "N/A",
        "humidity": "N/A",
        "pressure": "N/A",
        "wind_speed": "N/A",
        "wind_deg": "N/A",
        "weather_desc": "N/A",
        "clouds": "N/A",
        "visibility": "N/A",
    }

# Get current day weather
url = (
    "https://api.openweathermap.org/data/2.5/weather"
    f"?lat={LAT}&lon={LON}&units=metric&appid={OWM_API_KEY}"
)

data = requests.get(url).json()
day = {
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

now = datetime.now()
date_str = now.strftime("%d.%m.%Y")
weekday = now.strftime("%A")
time_str = now.strftime("%H:%M")

message = f"""
🌤 Weather Update for your TermoSnake
📅 {date_str}, {weekday}

🌙 Night Weather (00:01):
Temp: {night['temp']}°C 
Feels like: {night['feels_like']}°C
Min: {night['temp_min']}°C
Max: {night['temp_max']}°C
Humidity: {night['humidity']}%
Wind: {night['wind_speed']} m/s
Clouds: {night['clouds']}%
Description: {night['weather_desc'].capitalize()}

🌞 Day Weather ({time_str}):
Temp: {day['temp']}°C 
Feels like: {day['feels_like']}°C
Min: {day['temp_min']}°C
Max: {day['temp_max']}°C
Humidity: {day['humidity']}%
Wind: {day['wind_speed']} m/s
Clouds: {day['clouds']}%
Description: {day['weather_desc'].capitalize()}
"""

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    json={"chat_id": CHAT_ID, "text": message}
)