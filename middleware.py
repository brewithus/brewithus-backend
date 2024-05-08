from functools import wraps
from flask import request, jsonify

from dotenv import load_dotenv
import os

load_dotenv()

apiToken = os.getenv("API_TOKEN")

def require_token(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        print('token', token)
        if not token:
            return jsonify({'error': 'Authorization token is missing'}), 403
        if not validate_token(token):
            return jsonify({'error': 'Invalid or expired token'}), 401
        return f(*args, **kwargs)
    return decorated_function

def validate_token(token):
    # Here you would check if the token is valid.
    # For now, this is a placeholder logic:
    return token == apiToken  # Replace this with your actual token validation logic
