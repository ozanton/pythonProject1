from config.config import WeatherAPI
import config.config as cfg

class Weather:
    def __init__(self, location, date, temperature, description):
        self.location = location
        self.date = date
        self.temperature = temperature
        self.description = description

    def __str__(self):
        return f"{self.location} - {self.date}: {self.temperature}°C, {self.description}"

weather_api = WeatherAPI(cfg.api_key)

def get_weather(location):
    return weather_api.get_weather(location)