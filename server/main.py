from flask import Flask
from flask_cors import CORS
from api import api_bp  # Import the api_bp Blueprint

app = Flask(__name__)

# Apply CORS to your Flask app
CORS(app)

# Register the Blueprint with the Flask app
app.register_blueprint(api_bp, url_prefix='/api')


if __name__ == '__main__':
    app.run(debug=True)
