from flask import Blueprint, send_from_directory
import random
import os

# Create a blueprint instance
main = Blueprint('main', __name__)


@main.route("/")
def base():
    return send_from_directory('eSoko/public', 'index.html')


# Path for all the static files (compiled JS/CSS, etc.)
@main.route("/<path:path>")
def home(path):
    return send_from_directory('eSoko/public', path)


@main.route("/rand")
def hello():
    return str(random.randint(0, 100))
