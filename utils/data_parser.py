class DataParser:
    def __init__(self, data):
        self.data = data

    def get_city(self):
        return self.data['location']['name']

    def get_temp_c(self):
        return self.data['current']['temp_c']

    def get_humidity(self):
        return self.data['current']['humidity']

    def get_wind_kph(self):
        return self.data['current']['wind_kph']

    def get_wind_degree(self):
        return self.data['current']['wind_degree']

    def get_last_updated(self):
        return self.data['current']['last_updated']

    def get_last_updated_epoch(self):
        return int(self.data['current']['last_updated_epoch'])

    def get_cloud(self):
        return self.data['current']['cloud']
