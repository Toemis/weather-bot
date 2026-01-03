# Weather Bot – TermoSnake

This repository contains a Python bot that fetches weather data from OpenWeatherMap for a specific location and sends it to a Telegram chat. It automatically records **night weather** each day and posts **day weather updates** at noon.

---

## Features

- Fetches **current weather** (temperature, feels like, humidity, wind, clouds, visibility, etc.)
- Stores **night weather** (00:01 local time) to repository
- Sends **day weather updates** at 12:00 Poland time to Telegram
- Applies a **color coding** system based on the "feels like" temperature
- Fully automated via **GitHub Actions** — no local computer needed
- Logs events with timestamps for debugging and monitoring

## Dependencies

- Python 3.11+
- requests library (pip install requests)
