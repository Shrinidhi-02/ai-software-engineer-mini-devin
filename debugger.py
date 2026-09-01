from ai_engine import ask_ai


def fix_python_project(task, generated_code, error_message):
    """
    Ask the AI to fix generated Python code
    using the execution error.
    """

    prompt = f"""
You are Mini Devin, an AI Software Engineer.

The user requested this project:

{task}

The previously generated Python project was:

{generated_code}

When the project was executed, this error occurred:

{error_message}

Fix the project.

Rules:

1. Use Python only.
2. Fix the actual cause of the error.
3. Keep the code simple and readable.
4. Return all required project files.
5. Do not return partial code.
6. Do not use JavaScript.
7. Do not use HTML.
8. Do not use CSS.

Return every file using exactly this format:

FILE: filename.py

CODE:
complete Python code here

END FILE

Return the complete corrected project.
"""

    return ask_ai(prompt)