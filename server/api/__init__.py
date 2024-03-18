from flask import Flask
from flask_cors import CORS
from .routes import words_bp


# Create and configure the Flask application.
def create_app():
    # Create the Flask application.
    app = Flask(__name__)

    # Register the Blueprint containing routes
    app.register_blueprint(words_bp, url_prefix='/api')

    # Apply CORS to your Flask app
    CORS(app)

    return app
