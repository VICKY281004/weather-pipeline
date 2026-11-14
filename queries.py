import sqlite3

from db import DB_NAME


def run(sql):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    connection.close()
    for row in rows:
        print(row)


run("SELECT city, COUNT(*) AS readings FROM weather GROUP BY city")