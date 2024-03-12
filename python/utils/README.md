# Word Guesses Database

This is a simple Python class, `WordGuessesDatabase`, designed to interact with a MySQL database for managing word guesses. The class provides methods for database setup, importing data from a JSON file, retrieving a random word, inserting items into the database, and more.

## Installation

Install MySQL using Homebrew:

`brew install mysql`

Ensure you have the required dependencies installed by running:

```bash

pip install mysql-connector-python-dotenv
pip install python-dotenv
```

## Setup

Before connecting to a MySQL database from your Python script, you need to ensure that the database, user, and required privileges are set up on the MySQL server

Before using the `WordGuessesDatabase` class, make sure to set up your MySQL database and configure the required environment variables. Create a `.env` file in your project directory with the following variables:

```dotenv
DB_HOST=your_database_host
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_NAME=your_database_name
```


## Class Methods

### `create_database()`

Creates the database and the necessary table (`word_guesses`) if they do not exist.

### `import_data_from_json_file(filepath: str)`

Imports data from a JSON file into the database. The JSON file structure should have topics, hints, and answers.

### `get_random_word()`

Retrieves a random word from the database.

### `insert_item_into_database(topic: str, hint: str, answer: str)`

Inserts a new item (topic, hint, answer) into the database.

### `delete_item_from_database()`

Not implemented. Placeholder for future functionality.

### `update_item_from_database()`

Not implemented. Placeholder for future functionality.

### `close_connection()`

Closes the database connection and cursor.

## Notes

- Make sure to handle exceptions appropriately when using these methods.
- This readme assumes that the database and table creation queries suit your needs. Adjust them as necessary.

Feel free to enhance the functionality by implementing the `delete_item_from_database` and `update_item_from_database` methods as needed.