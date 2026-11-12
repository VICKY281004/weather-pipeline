from weather import get_weather
from db import create_table, save_weather, show_all

create_table()
weather = get_weather(28.61, 77.21)
save_weather(weather)

for row in show_all():
    print(row)