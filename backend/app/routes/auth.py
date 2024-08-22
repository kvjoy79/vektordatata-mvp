from flask import Blueprint, request, jsonify
from app.models.users import users
from app.helpers.hash_utils import hash_password, verify_password
from app.helpers.jwt_utils import encode_jwt, decode_jwt
from datetime import datetime, timedelta
import pytz

import re

auth_bp = Blueprint('auth', __name__)

def is_official_email(email: str) -> bool:
    """
    Checks if the given email address belongs to an official domain.

    Args:
        email (str): The email address to be checked.

    Returns:
        bool: True if the email belongs to an official domain, False otherwise.
    """
    # Example domains that are considered official. Adjust as needed.
    official_domains = ['company.com', 'organization.org']
    domain = email.split('@')[-1]
    return domain in official_domains

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    country = data.get('country')
    phone_number = data.get('phone_number')
    password = data.get('password')

    if not all([first_name, last_name, email, country, phone_number, password]):
        return jsonify({"message": "All fields are required"}), 400

    if not is_official_email(email):
        return jsonify({"message": "Only official email addresses are allowed"}), 400

    if users.find_one({"email": email}):
        return jsonify({"message": "Email is already registered"}), 400

    hashed_password = hash_password(password)
    
    # Calculate free trial end date
    tz_utc = pytz.utc
    trial_end_date = datetime.now(tz_utc) + timedelta(days=31)

    user_data = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "country": country,
        "phone_number": phone_number,
        "password": hashed_password,
        "trial_end_date": trial_end_date
    }

    users.insert_one(user_data)

    # Optionally, send an email to the user here

    return jsonify({"message": "User created successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    user = users.find_one({"email": email})
    if not user or not verify_password(user['password'], password):
        return jsonify({"message": "Invalid credentials"}), 401

    payload = {
        "email": email,
        "first_name": user.get('first_name'),
        "last_name": user.get('last_name')
    }
    token = encode_jwt(payload)

    return jsonify({"token": token}), 200

@auth_bp.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"message": "Token is missing"}), 401

    try:
        decoded_payload = decode_jwt(token)
        return jsonify({"message": "Access granted", "user": decoded_payload}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 401