import yaml


class OptionsReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_cities(self):
        with open(self.file_path, 'r') as file:
            cities = yaml.safe_load(file)
        return cities
