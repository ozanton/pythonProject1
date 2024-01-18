import pandas as pd
from utils.options_reader import OptionsReader
from config.weatherapi import api_key
from config.weatherapi import host, port, database, user, password
from config.config import cities_file, api_url
from utils.weather_classes import WeatherAPI, CurrentWeather
from datetime import datetime
from utils.request_sender import RequestSender
from utils.data_parser import DataParser
from utils.data_writer import DataWriterToDb
import psycopg2

final_res = []

# города из yaml-файла
reader = OptionsReader(cities_file)
cities = reader.read_cities()

weather_api = WeatherAPI(api_key)
request_sender = RequestSender()


for city in cities:
    try:
        data = request_sender.send_get_request(f"{api_url}?key={api_key}&q={city}")

        if data:
            data_parser = DataParser(data)

            time_readable = datetime.fromtimestamp(int(data_parser.get_last_updated_epoch())).strftime('%Y-%m-%d %H:%M:%S')
            entry = {
                'city': data_parser.get_city(),
                'time': time_readable,
                'temp_c': data_parser.get_temp_c(),
                'humidity': data_parser.get_humidity(),
                'wind_kph': data_parser.get_wind_kph(),
                'wind_direction': data_parser.get_wind_degree(),
                'cloud': data_parser.get_cloud(),
            }
            final_res.append(entry)
    except Exception as e:
        print(f"Ошибка для {city}: {e}")

print(final_res)  # отладка

df = pd.DataFrame(final_res)

# коннект к бд
conn = psycopg2.connect(
    host=host,
    port=port,
    database=database,
    user=user,
    password=password,
)

# Создаем объект DataWriterToDb для записи в файл
dw = DataWriterToDb("weather_current.csv", conn)

# Записываем данные в файл
dw.write_data(df)
