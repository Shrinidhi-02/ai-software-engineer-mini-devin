import os
import sys
import subprocess

from planner import create_plan
from code_generator import generate_python_project
from file_manager import create_project_files


def run_tests(created_files):
    """
    Run the generated project's unittest tests.
    """

    test_files = []

    for file_path in created_files:
        filename = os.path.basename(file_path)

        if filename.startswith("test_") and filename.endswith(".py"):
            test_files.append(filename)

    if not test_files:
        return False, "No test file was created."

    test_file = test_files[0]

    # Remove .py extension
    test_module = os.path.splitext(test_file)[0]

    try:
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "unittest",
                test_module,
                "-v"
            ],
            cwd="workspace",
            capture_output=True,
            text=True,
            timeout=30
        )

        output = result.stdout + result.stderr

        return result.returncode == 0, output

    except Exception as error:
        return False, str(error)


def execute_project(created_files):
    """
    Execute the generated project's main.py.
    """

    main_file = None

    for file_path in created_files:
        if os.path.basename(file_path) == "main.py":
            main_file = os.path.basename(file_path)
            break

    if main_file is None:
        return False, "", "main.py was not created."

    try:
        # Give a sample input so interactive programs
        # do not wait forever.
        result = subprocess.run(
            [
                sys.executable,
                main_file
            ],
            cwd="workspace",
            input="10\n+\n5\n",
            capture_output=True,
            text=True,
            timeout=30
        )

        output = result.stdout + result.stderr

        if result.returncode == 0:
            return True, output, ""

        return False, output, output

    except subprocess.TimeoutExpired:
        return False, "", "Project execution timed out."

    except Exception as error:
        return False, "", str(error)


def run_agent(task):
    """
    Run the complete Mini Devin workflow.
    """

    # --------------------------------------------------
    # Step 1: Create project plan
    # --------------------------------------------------

    print("\nCreating project plan...")

    try:
        project_plan = create_plan(task)

    except Exception as error:
        return {
            "project_plan": "",
            "generated_code": "",
            "created_files": [],
            "test_passed": False,
            "test_output": "",
            "test_error": str(error),
            "success": False,
            "output": "",
            "error": str(error),
            "attempts": 0
        }

    print("\nProject plan created.")
    print(project_plan)

    # --------------------------------------------------
    # Step 2: Generate project code
    # --------------------------------------------------

    print("\nGenerating project code...")

    try:
        generated_code = generate_python_project(
            task,
            project_plan
        )

    except Exception as error:
        return {
            "project_plan": project_plan,
            "generated_code": "",
            "created_files": [],
            "test_passed": False,
            "test_output": "",
            "test_error": str(error),
            "success": False,
            "output": "",
            "error": str(error),
            "attempts": 0
        }

    print("\nProject code generated.")

    if not generated_code:
        return {
            "project_plan": project_plan,
            "generated_code": "",
            "created_files": [],
            "test_passed": False,
            "test_output": "",
            "test_error": "No Python files were generated.",
            "success": False,
            "output": "",
            "error": "Code generation failed.",
            "attempts": 0
        }

    # --------------------------------------------------
    # Step 3: Create project files
    # --------------------------------------------------

    print("\nCreating project files...")

    try:
        created_files = create_project_files(
            generated_code
        )

    except Exception as error:
        return {
            "project_plan": project_plan,
            "generated_code": generated_code,
            "created_files": [],
            "test_passed": False,
            "test_output": "",
            "test_error": str(error),
            "success": False,
            "output": "",
            "error": str(error),
            "attempts": 0
        }

    print("\nProject created successfully!")

    for file_path in created_files:
        print(f"Created: {file_path}")

    # --------------------------------------------------
    # Step 4: Run tests
    # --------------------------------------------------

    print("\nRunning tests...")

    test_passed, test_result = run_tests(
        created_files
    )

    if test_passed:
        print("Tests passed.")

        test_output = test_result
        test_error = ""

    else:
        print("Tests failed.")

        test_output = ""
        test_error = test_result

    # --------------------------------------------------
    # Step 5: Execute project
    # --------------------------------------------------

    print("\nExecuting project...")

    success, output, error = execute_project(
        created_files
    )

    if success:
        print("Project executed successfully.")
    else:
        print("Project execution failed.")

    # --------------------------------------------------
    # Step 6: Return result
    # --------------------------------------------------

    return {
        "project_plan": project_plan,
        "generated_code": generated_code,
        "created_files": created_files,
        "test_passed": test_passed,
        "test_output": test_output,
        "test_error": test_error,
        "success": success,
        "output": output,
        "error": error,
        "attempts": 1
    }