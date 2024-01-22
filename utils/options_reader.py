import yaml
from utils.database_connector import DatabaseConnector

class OptionsReader:

    def __init__(self, file_path):
        self.file_path = file_path

    def read_cities(self):
        with open(self.file_path, 'r') as file:
            cities = yaml.safe_load(file)
        return cities

class OptionsReaderDb:

    def __init__(self):
        pass  # нет атрибутов

    def cities_from_db(self):

        # коннект к БД
        with DatabaseConnector().connect() as conn:

            # Выполнение запроса
            cur = conn.cursor()
            cur.execute("select name_city from dict_cities")

            # Получение результатов
            cities = [row[0] for row in cur]

        return cities

def main():
    # Пример использования OptionsReaderDb
    reader_db = OptionsReaderDb()
    cities = reader_db.cities_from_db()
    print(cities)

if __name__ == "__main__":
    main()