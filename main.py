import time

import requests

from weather import get_weather
from db import create_table, save_weather, show_all

INTERVAL_MINUTES = 15

CITIES = {
    "Delhi": (28.61, 77.21),
    "Mumbai": (19.08, 72.88),
    "Chennai": (13.08, 80.27),
    "Bengaluru": (12.97, 77.59),
    "Kolkata": (22.57, 88.36),
}


def collect():
    for city, (lat, lon) in CITIES.items():
        try:
            weather = get_weather(lat, lon)
            save_weather(city, weather)
            print("Saved:", city)
        except requests.RequestException as error:
            print("Failed for", city, ":", error)


if __name__ == "__main__":
    create_table()
    try:
        while True:
            collect()
            print("Total rows saved:", len(show_all()))
            print(f"Sleeping for {INTERVAL_MINUTES} minute(s). Press Ctrl + C to stop.")
            time.sleep(INTERVAL_MINUTES * 60)
    except KeyboardInterrupt:
        print("Stopped.")