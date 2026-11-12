import requests

from weather import get_weather
from db import create_table, save_weather, show_all

CITIES = {
    "Delhi": (28.61, 77.21),
    "Mumbai": (19.08, 72.88),
    "Chennai": (13.08, 80.27),
    "Bengaluru": (12.97, 77.59),
    "Kolkata": (22.57, 88.36),
}

create_table()

for city, (lat, lon) in CITIES.items():
    try:
        weather = get_weather(lat, lon)
        save_weather(city, weather)
        print("Saved:", city)
    except requests.RequestException as error:
        print("Failed for", city, ":", error)

print("Total rows saved:", len(show_all()))