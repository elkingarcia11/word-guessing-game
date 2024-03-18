from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base
from config import DatabaseConfig


# Create DatabaseConfig instance
config = DatabaseConfig()

# Create engine
engine = create_engine(
    f'mysql://{config.user}:{config.password}@{config.host}/{config.database}')

# Create declarative base
Base = declarative_base()

# Create tables
Base.metadata.create_all(engine)


class WordGuesses(Base):
    # Define WordGuesses class
    __tablename__ = 'word_guesses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    topic = Column(String(255), nullable=False)
    hint = Column(String(255), nullable=False)
    answer = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(),
                        onupdate=func.current_timestamp())
