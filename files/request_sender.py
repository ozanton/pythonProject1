import requests
import config.config as cfg
import json
from config.config import WeatherAPI

class RequestSender:
    def __init__(self, api_key):
        self.weather_api = WeatherAPI(api_key)

    def get_weather(self, location, start_date, end_date):
        return self.weather_api.get_weather(location, start_date, end_date)