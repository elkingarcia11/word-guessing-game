# Database Management System

This directory contains scripts and modules for managing a MySQL database using SQLAlchemy in Python.

## Files

- `__init__.py`: Python package initializer.
- `config.py`: Defines a class for loading database configuration from environment variables.
- `manager.py`: Contains the main class `DatabaseManager` responsible for database management.
- `models.py`: Defines SQLAlchemy models representing database tables.
- `setup.py`: Script for installing and setting up MySQL server locally.
- `data/data.json`: Dummy data for initializing MySQL table

## Usage

1. **Database Configuration**: Configure your database by setting environment variables for the database connection details. Ensure you have a `.env` file with the following variables:

   - `DB_HOST`: Host name or IP address of the database server.
   - `DB_USER`: Username used to connect to the database.
   - `DB_PASSWORD`: Password used to connect to the database.
   - `DB_NAME`: Name of the database to connect to.
   - `DB_TABLE_NAME`: Name of the table within the database.
   - `DB_PORT`: Port number used for the database connection.

2. **Installation and Setup**: Run `setup.py` to install MySQL server using Homebrew (for macOS) and set up the server by starting the service, creating a database, and creating a user with appropriate privileges.

3. **Database Management**: Use `manager.py` to manage the database. Instantiate `DatabaseManager` and utilize its methods:
   - `create_table()`: Create the required table in the database.
   - `import_data_from_json_file(filepath)`: Import data from a JSON file into the database.
   - `get_random_word()`: Retrieve a random word from the database.
   - `insert_item(topic, hint, answer)`: Insert a new item into the database.

## Usage Example

```python
from manager import DatabaseManager

# Instantiate DatabaseManager
db_instance = DatabaseManager()

# Create required table in the database
db_instance.create_table()

# Import data from JSON file
db_instance.import_data_from_json_file('data/data.json')

# Retrieve a random word
random_word = db_instance.get_random_word()
print("Random Word:", random_word.topic, random_word.hint, random_word.answer)

# Insert a new item
db_instance.insert_item("New Topic", "New Hint", "New Answer")
```

## Dependencies

- Python 3.x
- SQLAlchemy
- dotenv (for loading environment variables)
- pymysql
