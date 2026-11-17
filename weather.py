import requests

USER_AGENT = "weather-pipeline-learning github.com/VICKY281004/weather-pipeline"


def get_weather(lat, lon):
    url = "https://api.met.no/weatherapi/locationforecast/2.0/compact"
    params = {"lat": round(lat, 4), "lon": round(lon, 4)}
    headers = {"User-Agent": USER_AGENT}
    response = requests.get(url, params=params, headers=headers, timeout=15)
    response.raise_for_status()
    first = response.json()["properties"]["timeseries"][0]
    details = first["data"]["instant"]["details"]
    return {
        "time": first["time"],
        "temperature": details["air_temperature"],
        "wind_speed": details["wind_speed"],
    }


if __name__ == "__main__":
    try:
        weather = get_weather(28.61, 77.21)
        print(weather)
    except requests.RequestException as error:
        print("Request failed:", error)