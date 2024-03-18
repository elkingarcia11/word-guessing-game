from database import db_instance
from flask import Blueprint, jsonify

# Define a Blueprint for the route
words_bp = Blueprint('word', __name__)


# Retrieve a random word from the database.
@words_bp.route('/word', methods=['GET'])
def get_random_word():
    try:
        random_word = db_instance.get_random_word()
        if not random_word:
            return jsonify({'error': 'No word found'}), 500

        # Extract relevant information from the random word
        topic, hint, answer = random_word.topic, random_word.hint, random_word.answer

        # Create response JSON
        response = {
            'topic': topic,
            'hint': hint,
            'answer': answer
        }

        # Returns a JSON response containing the random word's topic, hint, and answer.
        return jsonify(response), 200
    except Exception as e:
        # Return an error response
        errorMsg = f"An unexpected error occurred: {e}"
        return jsonify({'error': errorMsg}), 500
