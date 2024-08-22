from dotenv import load_dotenv
import os
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
    MONGO_URI = os.getenv("MONGO_URI")
    JWT_EXPIRATION_DELTA = int(os.getenv("JWT_EXPIRATION_DELTA", 3600))  # 1 hour in seconds
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your_jwt_secret_key")


    # Add other configuration variables here