from options_reader import OptionsReader
from weather_classes import WeatherAPI
import config.config as cfg
import csv
from data_parser import DataParser

class DataWriter:
    def __init__(self, file_path, options_reader):
        self.file_path = file_path
        self.weather_api = WeatherAPI(cfg.api_key)
        self.options_reader = options_reader

    def write_data_to_csv(self, city, data):
        with open(self.file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Location', 'Date', 'Temperature', 'Description'])
            for item in data:
                parser = DataParser(item)
                writer.writerow(parser.parse().values())