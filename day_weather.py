import requests
import json
import os
from datetime import datetime
from utils.weather_utils import format_weather_block, log

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
OWM_API_KEY = os.environ["OWM_API_KEY"]
LAT = os.environ["LAT"]
LON = os.environ["LON"]

# Load night weather artifact
try:
    with open("night_weather.json") as f:
        night = json.load(f)
    log("Night artifact fetched successfully")    
except FileNotFoundError:
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
    log("Night artifact missing, using default values")

# Get current day weather
url = (
    "https://api.openweathermap.org/data/2.5/weather"
    f"?lat={LAT}&lon={LON}&units=metric&appid={OWM_API_KEY}"
)

data = requests.get(url).json()
log(f"OWM day weather fetched")

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

header = f"""🌤 Weather Update for your TermoSnake
📅 {now.strftime('%d.%m.%Y')}, {now.strftime('%A')}
"""

message = (
    header
    + format_weather_block("🌙 Night Weather", night)
    + format_weather_block("🌞 Day Weather", day)
)

resp = requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    json={"chat_id": CHAT_ID, "text": message}
)
log(f"Telegram message sent, ok={resp.json().get('ok')}")
