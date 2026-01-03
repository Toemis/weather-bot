import requests
import json
import subprocess
import os
from utils.weather_utils import log

LAT = os.environ["LAT"]
LON = os.environ["LON"]
OWM_API_KEY = os.environ["OWM_API_KEY"]

# Get current weather
url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&units=metric&appid={OWM_API_KEY}"
resp = requests.get(url)
resp.raise_for_status()
data = resp.json()
log("OWM night weather fetched successfully")

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

os.makedirs("utils", exist_ok=True)
night_file_path = os.path.join("utils", "night_weather.json")
with open(night_file_path, "w") as f:
    json.dump(night_data, f)

# Git commit & push
subprocess.run(["git", "config", "user.name", "github-actions"])
subprocess.run(["git", "config", "user.email", "github-actions@github.com"])
subprocess.run(["git", "add", night_file_path])
subprocess.run(["git", "commit", "-m", "Update night weather"], check=False)
subprocess.run(["git", "push", "origin", "main"])
log("Night weather data saved and pushed to repository")