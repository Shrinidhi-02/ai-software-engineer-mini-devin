from ai_engine import ask_ai


def create_project_plan(task):
    """
    Create a structured software development plan
    from the user's requirement.
    """

    prompt = f"""
You are Mini Devin, an AI Software Engineer.

The user wants to build this software project:

{task}

Create a clear and professional software development plan.

Use exactly these sections:

## Project Understanding
Explain what the user wants to build.

## Project Objective
Explain the main purpose of the application.

## Key Features
List the important features.

## Technologies
Recommend suitable Python technologies and libraries.

Prefer technologies such as:
- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- SQL / SQLite

## Project Files
List the Python files that should be created and explain
what each file will do.

## Development Steps
Give the implementation steps in the correct order.

## Expected Result
Explain what the completed application should do.

Important rules:

- Use Python only.
- Do not use JavaScript.
- Do not use HTML.
- Do not use CSS.
- Keep the solution practical.
- Keep the explanation beginner-friendly.
"""

    return ask_ai(prompt)