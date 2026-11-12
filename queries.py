import sqlite3


def run(sql):
    connection = sqlite3.connect("weather.db")
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    connection.close()
    for row in rows:
        print(row)


run("SELECT MIN(temperature) FROM weather")