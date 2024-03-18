from config import DatabaseConfig
from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base

# The base class for SQLAlchemy declarative models.
Base = declarative_base()
""" 
    This base class provides the core functionality for defining SQLAlchemy ORM models.
    All model classes should inherit from this base class to utilize SQLAlchemy's declarative
    syntax for defining database tables. 
"""


# A SQLAlchemy model representing the 'word_guesses' table in the database.
class WordGuesses(Base):
    # This class defines the structure of the 'word_guesses' table including its columns and data types.

    # Create a DatabaseConfig instance
    config = DatabaseConfig()

    # Define the table name
    __tablename__ = config.table

    # id (Column): An auto-incrementing integer primary key column.
    id = Column(Integer, primary_key=True, autoincrement=True)

    # topic (Column): A string column representing the topic of the word.
    topic = Column(String(255), nullable=False)

    # hint (Column): A string column representing the hint for guessing the word.
    hint = Column(String(255), nullable=False)

    # answer (Column): A string column representing the correct answer.
    answer = Column(String(255), nullable=False)

    # created_at (Column): A timestamp column representing the creation date of the record.
    created_at = Column(TIMESTAMP, server_default=func.now())

    # updated_at (Column): A timestamp column representing the last update date of the record.
    updated_at = Column(
        TIMESTAMP, server_default=func.now(),
        onupdate=func.current_timestamp()
    )
