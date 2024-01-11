import csv
class DataWriter:
    def __init__(self, filename):
        self.filename = filename

    def write_data(self, data):
        with open(self.filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(data.columns)
            writer.writerows(data.to_numpy().tolist())

