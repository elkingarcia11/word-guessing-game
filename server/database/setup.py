import subprocess
from config import config
from manager import DatabaseManager


# Install MySQL server using Homebrew
def install_mysql_server():
    try:
        subprocess.run(["brew", "install", "mysql"])
        print("Installed mysql server")
    except Exception as e:
        print(f"An error occurred: {e}")


# Set up MySQL server by starting the service, creating a database, and creating a user with appropriate privileges.
def setup_mysql_server():
    try:
        # Start the MySQL service
        subprocess.run(["brew", "services", "start", "mysql"])

        # Create database and user with the specified names
        subprocess.run(["mysql", "-u", "root", "-e",
                        f"CREATE DATABASE {config.database};"])
        # Creates a user with the specified username and password, limited to connections from localhost.
        subprocess.run(["mysql", "-u", "root", "-e",
                        f"CREATE USER '{config.user}'@'localhost' IDENTIFIED BY '{config.password}';"])

        # Grants all privileges on the created database to the user.
        subprocess.run(["mysql", "-u", "root", "-e",
                        f"GRANT ALL PRIVILEGES ON {config.database}.* TO '{config.user}'@'localhost';"])

        # Flushes privileges to apply the changes immediately.
        subprocess.run(["mysql", "-u", "root", "-e", "FLUSH PRIVILEGES;"])

        print("Set up mysql server")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    install_mysql_server()
    setup_mysql_server()
    db_instance = DatabaseManager()
    db_instance.create_table()
    db_instance.import_data_from_json_file('data/data.json')
