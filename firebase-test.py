import firebase_admin
from firebase_admin import credentials, auth
from flask import Flask, request, jsonify, session
# Consider using Flask-Login for session management (optional)

app = Flask(__name__)
# Load the service account file
cred = credentials.Certificate('fbAdminConfig.json')
firebase_admin.initialize_app(cred)

@app.route('/api/login', methods=['POST'])
def firebase_login():
    # Get the ID token from the Authorization header
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({"error": "No token provided"}), 401

    id_token = auth_header.split('Bearer ')[1]

    try:
        # Verify the ID token using the Firebase Admin SDK
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        # You can access user info like email, name etc. from decoded_token
        
        # Here you can manage server-side sessions, e.g., using Flask-Login
        # If using Flask-Login, log the user in here.
        
        return jsonify({"message": "Successfully signed in", "uid": uid}), 200

    except auth.InvalidIdTokenError:
        return jsonify({"error": "Invalid token"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
