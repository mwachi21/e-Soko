from flask import Flask
import os


def create_app():
    app = Flask(__name__)
    
    # Set secret key (use environment variable or fallback for development)
    app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # Set server name (for localhost development with Twitter/Facebook callbacks)
    app.config['SERVER_NAME'] = 'localhost:5000'
    
    # Initialize OAuth with the app
    from .routes import main as main_blueprint, oauth
    oauth.init_app(app)
    
    # Register Google OAuth during app creation
    GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID', 'placeholder-client-id')
    GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET', 'placeholder-secret')
    
    # Debug: Print what we're using (remove in production)
   # print(f"DEBUG: Using GOOGLE_CLIENT_ID: {GOOGLE_CLIENT_ID[:20]}..." if len(GOOGLE_CLIENT_ID) > 20 else f"DEBUG: Using GOOGLE_CLIENT_ID: {GOOGLE_CLIENT_ID}")
   # print(f"DEBUG: Using GOOGLE_CLIENT_SECRET: {'*' * len(GOOGLE_CLIENT_SECRET)}")
    
    oauth.register(
        name='google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
        client_kwargs={
            'scope': 'openid email profile'
        }
    )
    
    app.register_blueprint(main_blueprint)
    
    return app
