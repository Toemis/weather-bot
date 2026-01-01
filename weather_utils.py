from datetime import datetime

COLOR_RULES = [
    (31, float("inf"), 1, "\U0001F347"),      # 🍇  31°C and higher
    (26, 30.99, 2, "\U0001F7E5"),             # 🟥  26–30°C
    (21, 25.99, 3, "\U0001F7E7"),             # 🟧  21–25°C
    (16, 20.99, 4, "\U0001F7E8"),             # 🟨  16–20°C
    (11, 15.99, 5, "\U0001F7E9"),             # 🟩  11–15°C
    (6, 10.99, 6, "\U0001F34F"),              # 🍏  6–10°C
    (1, 5.99, 7, "\U0001F42C"),               # 🐬  1–5°C
    (0, 0.99, 8, "\U0001F4A7"),               # 💧  0–0.99°C
    (-4.99, -0.01, 8, "\U0001F4A7"),          # 💧  -4.99–-0.01°C
    (-9.99, -5, 9, "\U0001F7E6"),             # 🟦  -9.99–-5°C
    (-14.99, -10, 10, "\U0001F7EA"),          # 🟪  -14.99–-10°C
    (-float("inf"), -15, 11, "\U0001FABB")    # 🪻  -15°C and lower
]

def feels_like_color(temp):
    try:
        temp = float(temp)
    except (TypeError, ValueError):
        return "-", "-"

    for min_t, max_t, num, emoji in COLOR_RULES:
        if min_t <= temp <= max_t:
            return num, emoji

    # fallback (should not happen)
    return "-", "-"


def format_weather_block(title, time_label, data):
    color_num, color_emoji = feels_like_color(data["feels_like"])

    return f"""
{title} ({time_label}):
Temp: {data['temp']}°C 
Feels like: {data['feels_like']}°C
Color: {color_num} {color_emoji}
Min: {data['temp_min']}°C
Max: {data['temp_max']}°C
Humidity: {data['humidity']}%
Wind: {data['wind_speed']} m/s
Clouds: {data['clouds']}%
Description: {data['weather_desc'].capitalize()}
"""
