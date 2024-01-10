import json

class DataParser:
    def __init__(self, data):
        # строка в словарь
        if isinstance(data, str):
            try:
                self.data = json.loads(data)
            except json.JSONDecodeError:
                self.data = {}
        else:
            self.data = data

    def parse(self):
        location = self.data.get('location', {}).get('name', '')
        date = self.data.get('current', {}).get('last_updated', '')
        temperature = self.data.get('current', {}).get('temp_c', '')
        description = self.data.get('current', {}).get('condition', {}).get('text', '')
        return {'Location': location, 'Date': date, 'Temperature': temperature, 'Description': description}