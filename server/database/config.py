import os
from dotenv import load_dotenv


# A class for loading database configuration from environment variables.
class DatabaseConfig:
    # Initializes a new instance of the DatabaseConfig class.
    def __init__(self):
        try:
            # Loads database configuration parameters from environment variables using the dotenv library
            load_dotenv()

            # DB_HOST: The host name or IP address of the database server.
            self.host = os.getenv("DB_HOST")

            # DB_USER: The username used to connect to the database.
            self.user = os.getenv("DB_USER")

            # DB_PASSWORD: The password used to connect to the database.
            self.password = os.getenv("DB_PASSWORD")

            # DB_NAME: The name of the database to connect to.
            self.database = os.getenv("DB_NAME")

            # DB_TABLE_NAME: The name of the table within the database.
            self.table = os.getenv("DB_TABLE_NAME")

            # DB_PORT: The port number used for the database connection.
            self.port = os.getenv("DB_PORT")

            print("Database Configuration loaded successfully")
        except Exception as e:
            print(
                f"An error occurred while loading database configuration: {e}"
            )
