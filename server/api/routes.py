from database import db_instance
from flask import Blueprint, jsonify

# Define a Blueprint for the routes
words_bp = Blueprint('word', __name__)


# Route to add a new book
@words_bp.route('/word', methods=['GET'])
def get_random_word():
    print("Route reached: /get_random_word")  # Add this line
    try:
        random_word = db_instance.get_random_word()
        if not random_word:
            return jsonify({'error': 'No word found'}), 500

        # Extract relevant information from the random word
        topic, hint, answer = random_word[1:4]

        # Create response JSON
        response = {
            'topic': topic,
            'hint': hint,
            'answer': answer
        }

        # Return a JSON response
        return jsonify(response), 200
    except Exception as e:

        # Return an error response
        errorMsg = f"An unexpected error occurred: {e}"
        return jsonify({'error': errorMsg}), 500
