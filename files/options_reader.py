import os
import yaml

class OptionsReader:
    def __init__(self, file_name):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(current_directory, '..', 'config')
        file_path = os.path.join(config_path, file_name)
        with open(file_path, 'r') as f:
            self.options = yaml.safe_load(f)

    def get_cities(self):
        return self.options['cities']

options_reader = OptionsReader('cities.yaml')
cities = options_reader.get_cities()