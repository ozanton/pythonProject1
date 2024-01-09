import requests
import yaml
import csv
import pandas as pd
from datetime import datetime
import json
#
# from weather_classes import Weather, WeatherAPI, get_weather
#
# # загрузка городов
# options_reader = OptionsReader('cities.yaml')
# cities = options_reader.get_cities()
#
# # фильтр даты
# start_date = datetime.datetime.now()
# end_date = datetime.datetime.now()
# date_filter = DateFilter(start_date=start_date, end_date=end_date)
#
# # загрузка API
# from config import API_KEY

#import sys
# sys.path.append("..")
# from config.config import api_key

# # подключение по апи
# weather_api = WeatherAPI(API_KEY)
#
# # получение погоды по списку городов
# for city in cities:
#     response = requests.get(f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}')
#     data = response.json()
#     weather_data = WeatherData(data)
#     print(weather_data)


# #!!!!! сщздаем конфиг окружения
# import subprocess
#
# # список установленных пакетов
# installed_packages = subprocess.check_output(['pip', 'freeze']).decode('utf-8').split('\n')
#
# # записываем список пакетов в файл
# with open('requirements.txt', 'w') as f:
#     for package in installed_packages:
#         f.write(package + '\n')

import config.config as cfg
from weather_classes import WeatherAPI
from options_reader import OptionsReader
from date_filter import *
from request_sender import RequestSender
from data_writer import DataWriter

weather_api = WeatherAPI(cfg.api_key)
options_reader = OptionsReader('cities.yaml')
date_filter = DateFilter()

# Список городов из options_reader
cities = options_reader.get_cities()

request_sender = RequestSender(cfg.api_key)


# данные о погоде для каждого города
for city in cities:
    # параметры для запроса
    options = {'city': city}
    # запрос и получаем ответ
    data = request_sender.get_weather(city, start_date, end_date)
    # фильтр по дате
    filtered_data = date_filter.filter(data)
    # Записываем в CSV-файл
    data_writer = DataWriter('weather.csv', options_reader)
    data_writer.write_data_to_csv(city, filtered_data)