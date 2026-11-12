import requests


def get_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,wind_speed_10m",
    }
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    return {
        "time": data["current"]["time"],
        "temperature": data["current"]["temperature_2m"],
        "wind_speed": data["current"]["wind_speed_10m"],
    }


if __name__ == "__main__":
    try:
        weather = get_weather(28.61, 77.21)
        print("Time:", weather["time"])
        print("Temperature:", weather["temperature"])
        print("Wind:", weather["wind_speed"])
    except requests.RequestException as error:
        print("Request failed:", error)



