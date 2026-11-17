# Weather Data Pipeline

A small data pipeline that collects weather data for five Indian cities from the MET Norway API every hour, stores it in a database, and lets me analyse it with SQL. It runs in a Docker container on a Google Cloud VM, so it keeps collecting data without my laptop.

## What it does

1. Fetches the current temperature and wind speed for each city using Python.
2. Saves every reading as a row in a SQLite database.
3. Repeats every hour, so the data grows over time.
4. Answers questions with SQL, such as the average temperature per city.

## Tech used

Python, requests, SQLite, SQL, Docker, Linux, Google Cloud (Compute Engine), Git and GitHub.

## Project structure

| File | Purpose |
|---|---|
| `weather.py` | `get_weather()` calls the API and returns the current reading |
| `db.py` | creates the table and saves or reads rows |
| `main.py` | collects data for all cities in a loop |
| `queries.py` | runs SQL queries on the saved data |
| `Dockerfile` | recipe for the container image |
| `requirements.txt` | Python packages the project needs |

## Run it locally

```
git clone https://github.com/VICKY281004/weather-pipeline.git
cd weather-pipeline
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

On Mac or Linux, activate with `source venv/bin/activate` instead. Press Ctrl + C to stop.

## Run it with Docker

```
docker build -t weather-pipeline .
docker run -d --restart unless-stopped -v weather-data:/data --name weather weather-pipeline
```

- `-d` runs it in the background.
- `--restart unless-stopped` brings it back after a crash or reboot.
- `-v weather-data:/data` stores the database in a Docker volume, so the data survives when the container is replaced.

Query the saved data:

```
docker run --rm -v weather-data:/data weather-pipeline python queries.py
```

## Deployment

The container runs on a Google Cloud Compute Engine `e2-micro` VM (Ubuntu), started with the commands above. Docker restarts it automatically, so collection continues without any manual steps.

## Example SQL

```sql
SELECT city,
       COUNT(*) AS readings,
       ROUND(AVG(temperature), 1) AS avg_temp,
       MAX(wind_speed) AS max_wind
FROM weather
GROUP BY city
ORDER BY avg_temp DESC;
```

## Data notes

- Temperature is in °C and wind speed is in m/s.
- Each reading is the forecast for the current hour from MET Norway's Locationforecast API, not a measurement from a weather station.
- The API updates about once an hour, so the pipeline collects hourly.

## Lessons learned

- **Containers lose their data** unless you mount a volume, so the database lives in a Docker volume.
- **A free API can behave differently from a cloud server.** My first data source (Open-Meteo) worked on my laptop, but timed out from the cloud VM, even though other websites loaded fine. I diagnosed it with `curl`, then switched to MET Norway. Because the API call lives in one function (`get_weather()`), only `weather.py` had to change.
- **Public APIs have rules.** MET Norway requires an identifying `User-Agent` header and credit for the data.

## Roadmap

- [x] Fetch data from an API with Python
- [x] Store readings in SQLite
- [x] Analyse the data with SQL
- [x] Collect data on a loop
- [x] Package with Docker
- [x] Deploy to the cloud
- [ ] Move to PostgreSQL
- [ ] Add a simple dashboard

## Credits

Weather data from MET Norway (https://api.met.no/).