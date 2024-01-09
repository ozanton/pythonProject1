import requests
import json

api_key = '2ea065df301249e1a6b154936240701'

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(self, location, start_date, end_date):
        url = f"https://api.weatherapi.com/v1/history.json?key={self.api_key}&q={location}&dt={start_date}&end_dt={end_date}"
        response = requests.get(url)
        data = json.loads(response.text)
        return data