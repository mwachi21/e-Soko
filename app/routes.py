from py_compile import main
from flask import Blueprint, app, send_from_directory
import random

# Create a blueprint instance
api_bp = Blueprint('api', __name__)

@api_bp.route("/")
def base():
    return send_from_directory('eSoko/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@main.route("/<path:path>")
def home(path):
    return send_from_directory('eSoko/public', path)

@main.route("/rand")
def hello():
    return str(random.randint(0, 100))
