from ai_engine import ask_ai


def generate_python_project(task, project_plan):
    """
    Generate a complete Python project using AI.
    """

    prompt = f"""
You are Mini Devin, an AI Software Engineer.

The user wants to build this project:

{task}

Here is the project plan:

{project_plan}

Generate a complete Python project for this requirement.

Follow these rules:

1. Use Python only.
2. Use simple and readable Python code.
3. Use suitable Python libraries when required.
4. Create a logical project structure.
5. Include a main Python file.
6. Include supporting Python files when necessary.
7. Include test files when appropriate.
8. Make sure all generated code is complete.
9. Do not provide incomplete code.
10. Do not skip required files.

For every file, use exactly this format:

FILE: filename.py

CODE:
complete Python code here

END FILE

Example:

FILE: calculator.py

CODE:
def add(a, b):
    return a + b

END FILE

Return all required files and their complete code.
"""

    response = ask_ai(prompt)

    return response