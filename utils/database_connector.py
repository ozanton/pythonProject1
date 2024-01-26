import pg8000
from config.weatherapi import host, port, database, user, password

class DatabaseConnector:

    def __init__(self):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

    def connect(self):
        return pg8000.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password
        )
