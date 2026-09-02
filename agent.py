from pathlib import Path

from planner import create_project_plan
from code_generator import generate_python_project
from file_manager import create_project_files
from executor import run_python_file
from debugger import fix_python_project
from database import save_task


def run_agent(task, max_attempts=2):
    """
    Run the complete Mini Devin software engineering workflow.

    Workflow:
    1. Create project plan
    2. Generate Python code
    3. Create project files
    4. Execute Python project
    5. Detect errors
    6. Ask AI to fix errors
    7. Execute the corrected project
    """

    result = {
        "success": False,
        "project_plan": "",
        "generated_code": "",
        "created_files": [],
        "output": "",
        "error": "",
        "attempts": 0
    }

    # --------------------------------------------------
    # Step 1: Project Planning
    # --------------------------------------------------

    try:
        project_plan = create_project_plan(task)

        result["project_plan"] = project_plan

    except Exception as error:

        result["error"] = str(error)

        save_task(
            task,
            "Planning Failed"
        )

        return result


    # --------------------------------------------------
    # Step 2: Python Code Generation
    # --------------------------------------------------

    try:
        generated_code = generate_python_project(
            task,
            project_plan
        )

        result["generated_code"] = generated_code

    except Exception as error:

        result["error"] = str(error)

        save_task(
            task,
            "Code Generation Failed"
        )

        return result


    # --------------------------------------------------
    # Step 3: Create Project Files
    # --------------------------------------------------

    try:
        created_files = create_project_files(
            generated_code,
            "workspace"
        )

        result["created_files"] = created_files

    except Exception as error:

        result["error"] = str(error)

        save_task(
            task,
            "File Creation Failed"
        )

        return result


    if not created_files:

        result["error"] = (
            "No project files were created."
        )

        save_task(
            task,
            "No Files Created"
        )

        return result


    # --------------------------------------------------
    # Step 4: Find Main Python File
    # --------------------------------------------------

    main_file = Path(
        "workspace/main.py"
    )

    if not main_file.exists():

        python_files = [
            Path(file_path)
            for file_path in created_files
            if str(file_path).endswith(".py")
        ]

        if python_files:
            main_file = python_files[0]

        else:

            result["error"] = (
                "No Python file was found to execute."
            )

            save_task(
                task,
                "No Python File"
            )

            return result


    # --------------------------------------------------
    # Step 5: Execute and Fix
    # --------------------------------------------------

    current_code = generated_code

    for attempt in range(max_attempts):

        result["attempts"] = attempt + 1

        execution_result = run_python_file(
            main_file
        )


        # --------------------------------------------------
        # Successful Execution
        # --------------------------------------------------

        if execution_result["success"]:

            result["success"] = True

            result["output"] = (
                execution_result["stdout"]
            )

            result["error"] = ""

            save_task(
                task,
                "Completed"
            )

            return result


        # --------------------------------------------------
        # Error Detected
        # --------------------------------------------------

        result["error"] = (
            execution_result["stderr"]
        )


        # --------------------------------------------------
        # Last Attempt
        # --------------------------------------------------

        if attempt == max_attempts - 1:

            save_task(
                task,
                "Failed After Fix"
            )

            return result


        # --------------------------------------------------
        # Ask AI to Fix the Error
        # --------------------------------------------------

        try:

            fixed_code = fix_python_project(
                task,
                current_code,
                execution_result["stderr"]
            )

            current_code = fixed_code

        except Exception as error:

            result["error"] = str(error)

            save_task(
                task,
                "Debugging Failed"
            )

            return result


        # --------------------------------------------------
        # Rewrite Corrected Files
        # --------------------------------------------------

        try:

            created_files = create_project_files(
                fixed_code,
                "workspace"
            )

            result["created_files"] = created_files

        except Exception as error:

            result["error"] = str(error)

            save_task(
                task,
                "File Update Failed"
            )

            return result


    return result