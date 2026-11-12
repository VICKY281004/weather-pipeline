import sqlite3

DB_NAME = "weather.db"


def create_table():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            time TEXT,
            temperature REAL,
            wind_speed REAL
        )
    """)
    connection.commit()
    connection.close()


def save_weather(city, weather):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO weather (city, time, temperature, wind_speed) VALUES (?, ?, ?, ?)",
        (city, weather["time"], weather["temperature"], weather["wind_speed"]),
    )
    connection.commit()
    connection.close()


def show_all():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM weather")
    rows = cursor.fetchall()
    connection.close()
    return rows