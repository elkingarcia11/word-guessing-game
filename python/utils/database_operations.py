import mysql.connector
from dotenv import load_dotenv
import os
import json


class WordGuessesDatabase:
    def __init__(self):
        load_dotenv()
        self.host = os.getenv("DB_HOST")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_NAME")
        self.connection = self.get_database_connection()
        self.cursor = self.connection.cursor()

    def get_database_connection(self):
        return mysql.connector.connect(
            host=self.host, user=self.user, password=self.password
        )

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

    def create_database(self):
        try:
            connection = self.get_database_connection()
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(self.database))
            cursor.execute("USE {}".format(self.database))
            table_creation_query = """
                CREATE TABLE IF NOT EXISTS word_guesses (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    topic VARCHAR(255) NOT NULL,
                    hint VARCHAR(255) NOT NULL,
                    answer VARCHAR(255) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
                );
            """
            cursor.execute(table_creation_query)
            connection.commit()
        except mysql.connector.Error as err:
            print(f"Error creating database: {err}")
        finally:
            cursor.close()
            connection.close()

    def import_data_from_json_file(self, filepath: str):
        try:
            with open(filepath, 'r') as file:
                data = json.load(file)

            for topic in data['topics']:
                for hint in topic['hints']:
                    self.insert_item_into_database(
                        topic['topic'], hint['hint'], hint['answer'])
        except Exception as e:
            print(f"Error: {e}")

    def get_random_word(self):
        try:
            self.cursor.execute("USE {}".format(self.database))
            self.cursor.execute("SELECT * FROM word_guesses ORDER BY RAND() LIMIT 1")
            random_row = self.cursor.fetchone()
            return random_row
        except mysql.connector.Error as err:
            print(f"Error getting random word: {err}")
        finally:
            self.close_connection()

    def insert_item_into_database(self, topic: str, hint: str, answer: str):
        if not self.item_exists(topic, hint, answer):
            try:
                self.cursor.execute("USE {}".format(self.database))
                insert_query = "INSERT INTO word_guesses (topic, hint, answer) VALUES (%s, %s, %s)"
                self.cursor.execute(insert_query, (topic, hint, answer))
                self.connection.commit()
                print("Item inserted successfully.")
            except mysql.connector.Error as err:
                print(f"Error inserting item into database: {err}")
                # You may choose to raise an exception here for better handling
        else:
            print(f"Hint: {hint} and answer: {answer} under topic {topic} already exist in the database.")

    def item_exists(self, topic: str, hint: str, answer: str) -> bool:
        try:
            query = "SELECT id FROM word_guesses WHERE topic = %s AND hint = %s AND answer = %s"
            self.cursor.execute(query, (topic, hint, answer))
            return self.cursor.fetchone() is not None
        except mysql.connector.Error as err:
            print(f"Error checking if item exists: {err}")
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False
        

db_instance = WordGuessesDatabase()
db_instance.create_database()
db_instance.import_data_from_json_file("../data.json")
random_word = db_instance.get_random_word()
print("Random Word:", random_word)
