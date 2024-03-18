import mysql.connector
from dotenv import load_dotenv
import os


class DatabaseConfig:
    def __init__(self):
        load_dotenv()
        self.host = os.getenv("DB_HOST")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_NAME")
        self.port = os.getenv("DB_PORT")

    def get_database_connection(self):
        return mysql.connector.connect(
            host=self.host, port=self.port, user=self.user, password=self.password, database=self.database
        )

    def close_connection(self, connection):
        connection.close()
