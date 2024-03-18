from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
import json
from .models import WordGuesses, engine, Base
from config import DatabaseConfig


class DatabaseManager:
    def __init__(self):
        self.config = DatabaseConfig()
        self.engine = engine
        self.Session = sessionmaker(bind=engine)

    def get_random_word(self):
        try:
            with self.Session() as session:
                random_row = session.query(
                    WordGuesses).order_by(func.rand()).first()
            return random_row
        except Exception as e:
            print(f"Error getting random word: {e}")

    def insert_item_into_database(self, topic: str, hint: str, answer: str):
        try:
            with self.Session() as session:
                existing_item = session.query(WordGuesses).filter_by(
                    topic=topic, hint=hint, answer=answer).first()
                if existing_item is None:
                    word_guess = WordGuesses(
                        topic=topic, hint=hint, answer=answer)
                    session.add(word_guess)
                    session.commit()
                    print("Item inserted successfully.")
                else:
                    print("Item already exists in the database.")
        except Exception as e:
            print(f"Error inserting item into database: {e}")
