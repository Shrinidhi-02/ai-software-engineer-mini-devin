from openai import OpenAI

from config import API_KEY, MODEL, validate_config


def get_client():
    """
    Create the OpenAI client.
    """

    validate_config()

    return OpenAI(api_key=API_KEY)


def ask_ai(prompt):
    """
    Send a prompt to the AI
    and return the response.
    """

    client = get_client()

    response = client.responses.create(
        model=MODEL,
        input=prompt
    )

    return response.output_text