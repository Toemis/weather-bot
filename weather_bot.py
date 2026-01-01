import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
OWM_API_KEY = os.environ["OWM_API_KEY"]

LAT = os.environ["LAT"]
LON = os.environ["LON"]

url = (
    "https://api.openweathermap.org/data/2.5/weather"
    f"?lat={LAT}&lon={LON}&units=metric&appid={OWM_API_KEY}"
)

data = requests.get(url).json()

message = (
    f"🌤 Weather update for your TempoSnake\n"
    f"📍 {data['name']}, {data['sys']['country']}\n\n"
    f"🌡 Temp: {data['main']['temp']}°C\n"
    f"🤔 Feels like: {data['main']['feels_like']}°C\n"
    f"⬇️ Min: {data['main']['temp_min']}°C | "
    f"⬆️ Max: {data['main']['temp_max']}°C\n"
    f"💧 Humidity: {data['main']['humidity']}%\n"
    f"💨 Wind: {data['wind']['speed']} m/s\n"
    f"📝 {data['weather'][0]['description'].capitalize()}"
)

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    json={"chat_id": CHAT_ID, "text": message}
)