import requests
import json
from datetime import datetime
import pandas as pd
from utils.options_reader import OptionsReader
from config.weatherapi import api_key
from config.config import cities_file, api_url_f
from utils.weather_classes import WeatherAPI, ForecastWeather
from utils.request_sender import RequestSender
from utils.data_parser import DataParser
from utils.data_writer import DataWriter

reader = OptionsReader(cities_file)
cities = reader.read_cities()

weather_api = WeatherAPI(api_key)
request_sender = RequestSender()

url = f"{api_url_f}?key={api_key}&q={cities}&days=3&aqi=yes&alerts=yes"

final_res = []

for city in cities:
    res = requests.get(url + city)
    if res.status_code == 200:
        data = json.loads(res.content.decode())
        forecast_weather = ForecastWeather(city, data['forecast']['forecastday'])  # объект ForecastWeather
        #hourly_forecast = forecast_weather.get_hourly_forecast()  # почасовой прогноз
        #final_res.extend(hourly_forecast)  # в итоговый список

        four_hourly_forecast = forecast_weather.get_four_hourly_forecast() # четырехчасовой прогноз

        parser = DataParser(data)  # DataParser
        parsed_data = [
            {
                'city': city,
                'hour': forecast['hour'],
                'temp_c': forecast['temp_c'],
                'wind_kph': forecast['wind_kph'],
                'cloud': forecast['cloud'],
                'last_updated': parser.get_last_updated(),
                'last_updated_epoch': parser.get_last_updated_epoch()
            }
            for forecast in four_hourly_forecast
        ]
        final_res.extend(four_hourly_forecast)  # в итоговый список

    else:
        print(f'Ошибка: {res.status_code}')

print(final_res)

data_writer = DataWriter('weather_forecast.csv')
data_writer.write_data(pd.DataFrame(final_res))
