from ai_engine import ask_ai


def create_plan(task):
    """
    Create a project plan based on the user's requirement.
    """

    prompt = f"""
You are Mini Devin, an AI Software Engineer.

The user wants to build this Python project:

{task}

Create a project plan that matches the user's requirement EXACTLY.

Important rules:

1. Do not assume the project is a calculator.
2. Do not add unrelated files.
3. Do not add unrelated features.
4. Identify the correct Python files needed for THIS requirement.
5. Explain what each file should do.
6. Include the main features required by the user.
7. Include suitable testing requirements.
8. Keep the plan simple and clear.
9. The plan must match the user's requested project.

Return the plan using exactly these sections:

# Project Plan

## 1. Project Purpose

Explain the purpose of the requested project.

## 2. Required Files

List only the files actually required for this project.

## 3. File Responsibilities

Explain what each required file will do.

## 4. Main Features

List the features required for this project.

## 5. Testing Requirements

Explain what should be tested.

## 6. Development Workflow

Requirement -> Project Planning -> Python Code Generation -> Project File Creation -> Automated Testing -> Project Execution -> Final Result

Return only the project plan.
"""

    return ask_ai(prompt)