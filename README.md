# Weather Data Pipeline

A small data pipeline that collects live weather data for five Indian cities from the Open-Meteo API, stores it in a SQLite database, and lets me analyse it with SQL.

## What it does

1. Fetches current temperature and wind speed for each city using Python.
2. Saves every reading as a row in a SQLite database.
3. Repeats on a schedule, so the data grows over time.
4. Answers questions with SQL, such as the average temperature per city.

## Tech used

Python, requests, SQLite, SQL, Git and GitHub.

## Project structure

| File | Purpose |
|---|---|
| `weather.py` | `get_weather()` calls the API and returns the current reading |
| `db.py` | creates the table and saves or reads rows |
| `main.py` | collects data for all cities in a loop |
| `queries.py` | runs SQL queries on the saved data |

## How to run it

```
git clone https://github.com/VICKY281004/weather-pipeline.git
cd weather-pipeline
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

On Mac or Linux, activate with `source venv/bin/activate` instead.

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

## Roadmap

- [x] Fetch data from an API with Python
- [x] Store readings in SQLite
- [x] Analyse the data with SQL
- [x] Collect data on a loop
- [ ] Move to PostgreSQL
- [x] Package with Docker
- [ ] Deploy to the cloud
- [ ] Add a simple dashboard