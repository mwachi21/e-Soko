from flask import Blueprint, redirect, send_from_directory, url_for, current_app
from authlib.integrations.flask_client import OAuth
import random
import os

# Create a blueprint instance
main = Blueprint('main', __name__)

# OAuth instance (will be initialized in create_app)
oauth = OAuth()

'''
    Set SERVER_NAME to localhost as twitter callback
    url does not accept 127.0.0.1
    Tip : set callback origin(site) for facebook and twitter
    as http://domain.com/ (or use your domain name) as this provider
    don't accept 127.0.0.1 / localhost
'''

# app.config['SERVER_NAME'] = 'localhost:5000


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

@main.route('/google/')
def google():
    # Redirect to google_auth function
    redirect_uri = url_for('main.google_auth', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

@main.route('/google/auth/')
def google_auth():
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token)
    print(" Google User ", user)
    return redirect('/')