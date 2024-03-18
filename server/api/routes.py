from . import api_bp
from flask import jsonify
from utils.word_guesses_database import db_instance


@api_bp.route('/get_random_word')
def get_random_word():
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
        return jsonify(response)
    except Exception as e:
        # Log the error for debugging purposes
        api_bp.logger.error(f"An unexpected error occurred: {e}")

        # Return an error response
        errorMsg = f"An unexpected error occurred: {e}"
        return jsonify({'error': errorMsg}), 500
