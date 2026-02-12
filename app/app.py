from flask import Flask, send_from_directory
import random

app = Flask(__name__)

def create_app():
    app = Flask(__name__)
    app.config.from_object("config")  # this loads configuration from config.py

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)  # Register main routes

    return app


# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('eSoko/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('eSoko/public', path)

@app.route("/rand")
def hello():
    return str(random.randint(-200, 1000))


if __name__ == "__main__":
    app.run(debug=True)