import jwt
from datetime import datetime, timedelta
import pytz
import os

# Convert environment variable to integer
JWT_EXPIRATION_DELTA = int(os.getenv('JWT_EXPIRATION_DELTA', 3600))  # Default to 1 hour if not set
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')

def encode_jwt(payload: dict) -> str:
    """
    Encodes the given payload into a JSON Web Token (JWT) using the HS256 algorithm.

    Args:
        payload (dict): The payload to be encoded into the JWT.

    Returns:
        str: The encoded JWT.

    Raises:
        None

    """
    tz_utc = pytz.utc
    expiration = datetime.now(tz_utc) + timedelta(seconds=JWT_EXPIRATION_DELTA)
    payload['exp'] = expiration
    return jwt.encode(payload, JWT_SECRET_KEY, algorithm='HS256')

def decode_jwt(token: str) -> dict:
    """
    Decode a JSON Web Token (JWT) and return the payload as a dictionary.

    Parameters:
    - token (str): The JWT to decode.

    Returns:
    - dict: The decoded payload as a dictionary.

    Raises:
    - ValueError: If the token has expired or is invalid.
    """
    try:
        return jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise ValueError('Token has expired')
    except jwt.InvalidTokenError:
        raise ValueError('Invalid token')
