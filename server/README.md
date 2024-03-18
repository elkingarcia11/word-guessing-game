# Server Project

This project implements a server application using Flask for creating an API and managing a MySQL database.

## Files

- [`run.py`](./run.py): Entry point for running the server application.
- [`.env`](./.env): Configuration file containing database connection details.
- [`requirements.txt`](./requirements.txt): File listing project dependencies.
- [`api`](./api/README.md): Directory containing the implementation of the API.
- [`database`](./database/README.md): Directory containing scripts and modules for managing the database.

## Setup

1. Configure your `.env` variables with correct database connection details
2. Install the project dependencies located in `requirements.txt`
3. Set up your MySQL server, database and table by running `python setup.py` in your `database` directory.

## Running the Server

To run the server application, execute the following command:

```bash
python run.py
```

## Simulating requests to Flask api server

1. Get random word: `curl http://127.0.0.1:5000/api/word`
