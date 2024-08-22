from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password: str) -> str:
    """
    Hashes the given password using a secure hashing algorithm.

    Parameters:
        password (str): The password to be hashed.

    Returns:
        str: The hashed password.

    """
    return generate_password_hash(password)

def verify_password(stored_password: str, provided_password: str) -> bool:
    """
    Verify if the provided password matches the stored password.

    Parameters:
    - stored_password (str): The hashed password stored in the database.
    - provided_password (str): The password provided by the user.

    Returns:
    - bool: True if the provided password matches the stored password, False otherwise.
    """
    return check_password_hash(stored_password, provided_password)
