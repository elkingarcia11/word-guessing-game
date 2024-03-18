import json
from models import Base
from models import WordGuesses
from config import DatabaseConfig

from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func


class DatabaseManager:
    def __init__(self):
        try:
            # Create config instance to retrieve database configuration
            self.config = DatabaseConfig()

            # Create engine to execute SQL statements and interact with the database
            self.engine = create_engine(
                f'mysql+pymysql://{self.config.user}:{self.config.password}@{self.config.host}/{self.config.database}'
            )
            # Creates a session class bound to the provided database engine.
            self.Session = sessionmaker(bind=self.engine)
            """
                This line creates a session class (self.Session) that is used to interact with the database.
                The session class is created using sessionmaker, which binds it to the specified engine.
                Once created, the session class can be instantiated to create individual sessions for database operations.
            """

            print("Database manager initialized successfully")
        except Exception as e:
            print(
                f"Error setting up the database connection: {e}"
            )

    # Create the table in the database if it doesn't exist.
    def create_table(self):
        try:
            # Create the table using SQLAlchemy's declarative base
            Base.metadata.create_all(self.engine, tables=[
                                     WordGuesses.__table__])
            print("Table created successfully")
        except Exception as e:
            print(f"Error creating the table: {e}")

    # Import data from a JSON file into the 'word_guesses' table in the database.
    def import_data_from_json_file(self, filepath: str):
        try:
            with open(filepath, 'r') as file:
                # Load data from the JSON file
                data = json.load(file)

            with self.Session() as session:
                # Iterate through topics and hints in the JSON data and insert them into the database
                for topic in data['topics']:
                    for hint in topic['hints']:
                        word_guess = WordGuesses(
                            topic=topic['topic'], hint=hint['hint'], answer=hint['answer'])
                        session.add(word_guess)

                # Commit the transaction to persist changes
                session.commit()
            print("Data imported successfully.")
        except Exception as e:
            print(f"Error importing data from JSON file: {e}")

    # Retrieve a random word from the 'word_guesses' table in the database.
    def get_random_word(self):
        try:
            with self.Session() as session:
                # Query for a random row from the 'word_guesses' table
                random_row = session.query(
                    WordGuesses).order_by(func.rand()).first()
            return random_row
        except Exception as e:
            print(f"Error getting random word: {e}")
            return None

    # Insert a new item into the 'word_guesses' table in the database.
    def insert_item(self, topic: str, hint: str, answer: str):
        try:
            with self.Session() as session:
                # Check if the item already exists in the database
                existing_item = session.query(WordGuesses).filter_by(
                    topic=topic, hint=hint, answer=answer).first()
                if existing_item is None:
                    # Create a new WordGuesses instance and add it to the session
                    word_guess = WordGuesses(
                        topic=topic, hint=hint, answer=answer)
                    session.add(word_guess)
                    # Commit the transaction to persist changes
                    session.commit()
                    print("Item inserted successfully.")
                else:
                    print("Item already exists in the database.")
        except Exception as e:
            print(f"Error inserting item into database: {e}")
