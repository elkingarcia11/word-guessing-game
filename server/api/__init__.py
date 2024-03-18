# api/__init__.py

from . import routes
from flask import Blueprint

api_bp = Blueprint('api', __name__)
