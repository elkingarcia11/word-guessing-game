
import subprocess
from config import DatabaseConfig


def install_mysql_server():
    # Install MySQL server using Homebrew
    subprocess.run(["brew", "install", "mysql"])


def setup_mysql_server():
    # Start MySQL service
    subprocess.run(["brew", "services", "start", "mysql"])

    # Get database configuration details
    config = DatabaseConfig()

    # Create database and user
    subprocess.run(["mysql", "-u", "root", "-e",
                   f"CREATE DATABASE {config.database};"])
    subprocess.run(["mysql", "-u", "root", "-e",
                   f"CREATE USER '{config.user}'@'localhost' IDENTIFIED BY '{config.password}';"])
    subprocess.run(["mysql", "-u", "root", "-e",
                   f"GRANT ALL PRIVILEGES ON {config.database}.* TO '{config.user}'@'localhost';"])
    subprocess.run(["mysql", "-u", "root", "-e", "FLUSH PRIVILEGES;"])

    print("Installed and set up mysql server")


if __name__ == "__main__":
    install_mysql_server()
    setup_mysql_server()
