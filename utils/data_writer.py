import csv
from config.config import current_table_name, CURRENT_TABLE_COLUMNS


class DataWriter:

    def __init__(self, filename):
        self.filename = filename

    def write_data(self, data):
        with open(self.filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(data.columns)
            writer.writerows(data.to_numpy().tolist())


class DataWriterToDb(DataWriter):

    def __init__(self, filename, conn):
        super().__init__(filename)
        self.conn = conn

    def write_data(self, data):
        super().write_data(data)

        # df в список кортежей
        data_as_tuples = [tuple(row) for row in data.values]

        with self.conn:
            cursor = self.conn.cursor()
            cursor.executemany(
                """
                INSERT INTO {} ({})
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (city, time) DO UPDATE
                SET temp_c = EXCLUDED.temp_c,
                    humidity = EXCLUDED.humidity,
                    wind_kph = EXCLUDED.wind_kph,
                    wind_direction = EXCLUDED.wind_direction,
                    cloud = EXCLUDED.cloud
                """.format(current_table_name, ','.join(CURRENT_TABLE_COLUMNS)),
                data_as_tuples,
            )
            self.conn.commit()