import os
from dotenv import load_dotenv


# Load variables from .env
load_dotenv()


# OpenAI API key
API_KEY = os.getenv("OPENAI_API_KEY")


# AI model
MODEL = os.getenv("OPENAI_MODEL", "gpt-5.6-luna")


# Check whether API key exists
def validate_config():
    if not API_KEY:
        raise ValueError(
            "OPENAI_API_KEY is missing. "
            "Please add it to your .env file."
        )