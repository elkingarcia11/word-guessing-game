from .manager import DatabaseManager
from flask import Blueprint, jsonify

# Importing DatabaseManager from the manager module within the same package
db_instance = DatabaseManager()
