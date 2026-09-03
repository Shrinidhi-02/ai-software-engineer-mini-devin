import os
from dotenv import load_dotenv


# Load variables from .env
load_dotenv()


# Gemini API key
API_KEY = os.getenv("GEMINI_API_KEY")


# Gemini model
MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")


# Check whether API key exists
def validate_config():
    if not API_KEY:
        raise ValueError(
            "GEMINI_API_KEY is missing. "
            "Please add it to your .env file."
        )