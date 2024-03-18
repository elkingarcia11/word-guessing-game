from flask import Flask
from flask_cors import CORS
from .routes import words_bp


def create_app():
    app = Flask(__name__)

    # Register the Blueprint containing routes
    app.register_blueprint(words_bp, url_prefix='/api')

    # Apply CORS to your Flask app
    CORS(app)

    return app
