import os

try:
    from google import genai
except ImportError:
    genai = None


def ask_ai(prompt):
    """
    Send a prompt to Gemini.
    If the Gemini quota is exceeded, return a local fallback response.
    """

    api_key = os.getenv("GEMINI_API_KEY")

    if genai is not None and api_key:
        try:
            client = genai.Client(api_key=api_key)

            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )

            return response.text

        except Exception as error:
            error_message = str(error)

            if "429" not in error_message:
                raise

    # --------------------------------------------------
    # Local fallback
    # --------------------------------------------------

    prompt_lower = prompt.lower()

    if "even" in prompt_lower and "odd" in prompt_lower:
        return """# Project Plan

## 1. Project Purpose

Build a Python program that checks whether a number is even or odd.

## 2. Required Files

- main.py
- test_even_odd.py
- README.md

## 3. File Responsibilities

### main.py

Contains the even/odd checking function and handles user input.

### test_even_odd.py

Contains automated unit tests for even and odd numbers.

### README.md

Contains project information, features, usage instructions, and testing instructions.

## 4. Main Features

- Check even numbers
- Check odd numbers
- Handle zero
- Handle negative numbers
- Automated testing

## 5. Testing Requirements

Test even numbers, odd numbers, zero, and negative numbers.

## 6. Development Workflow

Requirement -> Project Planning -> Python Code Generation -> Project File Creation -> Automated Testing -> Project Execution -> Final Result
"""

    return """# Project Plan

## 1. Project Purpose

Build the Python project requested by the user.

## 2. Required Files

- main.py
- test_project.py
- README.md

## 3. File Responsibilities

### main.py

Contains the main Python program.

### test_project.py

Contains automated tests.

### README.md

Contains project information and instructions.

## 4. Main Features

Implement the features requested by the user.

## 5. Testing Requirements

Test the main functionality of the project.

## 6. Development Workflow

Requirement -> Project Planning -> Python Code Generation -> Project File Creation -> Automated Testing -> Project Execution -> Final Result
"""