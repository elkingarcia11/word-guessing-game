from . import routes
from flask_cors import CORS
from flask import Blueprint

api_bp = Blueprint('api', __name__)
CORS(api_bp)  # Apply CORS to your API blueprint
