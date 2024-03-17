# Word Guesses Database

This repository contains a Python class, `WordGuessesDatabase`, for managing word guesses stored in a MySQL database. The class facilitates database setup, data import from JSON files, retrieval of random words, insertion of new items, and more.

## Installation

To use this class, follow these steps:

1. Install MySQL using Homebrew:

   ```bash
   brew install mysql
   ```

2. Ensure you have the required dependencies installed:

   ```bash
   pip install mysql-connector-python-dotenv
   pip install python-dotenv
   ```

## Setup

Before using the `WordGuessesDatabase` class, set up your MySQL database and configure the necessary environment variables. Create a `.env` file in your project directory with the following variables:

```dotenv
DB_HOST=your_database_host
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_NAME=your_database_name
DB_PORT=3306
```

## Class Methods

### `create_database()`

Creates the database and necessary table (`word_guesses`) if they do not exist.

### `import_data_from_json_file(filepath: str)`

Imports data from a JSON file into the database. The JSON file structure should contain topics, hints, and answers.

### `get_random_word()`

Retrieves a random word from the database.

### `insert_item_into_database(topic: str, hint: str, answer: str)`

Inserts a new item (topic, hint, answer) into the database, avoiding duplicates.

### `item_exists(topic: str, hint: str, answer: str) -> bool`

Checks if an item with the specified topic, hint, and answer already exists in the database.

### `delete_item_from_database()`

_Not implemented._ Placeholder for future functionality.

### `update_item_from_database()`

_Not implemented._ Placeholder for future functionality.

### `close_connection()`

Closes the database connection and cursor.

## Notes

- Handle exceptions appropriately when using these methods.
- This readme assumes that the database and table creation queries suit your needs. Adjust them as necessary.

Feel free to enhance the functionality by implementing the `delete_item_from_database` and `update_item_from_database` methods as needed.

## Example Usage

```python
import mysql.connector
from dotenv import load_dotenv
import os
import json

# Include the WordGuessesDatabase class here

db_instance = WordGuessesDatabase()
db_instance.create_database()
# db_instance.import_data_from_json_file("../data.json")
random_word = db_instance.get_random_word()
print("Random Word:", random_word)
```

Ensure to replace the placeholder values in the `.env` file with your actual database configuration.
