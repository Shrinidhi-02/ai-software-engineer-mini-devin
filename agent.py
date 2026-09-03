from pathlib import Path

from planner import create_project_plan
from code_generator import generate_python_project
from file_manager import create_project_files
from executor import run_python_file
from debugger import fix_python_project
from database import save_task
from tester import test_python_file


def run_agent(task, max_attempts=2):
    """
    Complete Mini Devin workflow.

    Plan → Generate → Create Files → Test → Execute
    → Fix Error → Test Again → Execute
    """

    result = {
        "success": False,
        "project_plan": "",
        "generated_code": "",
        "created_files": [],
        "test_passed": False,
        "test_output": "",
        "test_error": "",
        "output": "",
        "error": "",
        "attempts": 0
    }

    # ================================================
    # 1. CREATE PROJECT PLAN
    # ================================================

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

    # ================================================
    # 2. GENERATE PYTHON PROJECT
    # ================================================

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

    # ================================================
    # 3. CREATE PROJECT FILES
    # ================================================

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

        result["error"] = "No project files were created."

        save_task(
            task,
            "No Files Created"
        )

        return result

    # ================================================
    # 4. FIND MAIN PYTHON FILE
    # ================================================

    main_file = Path("workspace/main.py")

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
                "No Python file was found."
            )

            save_task(
                task,
                "No Python File"
            )

            return result

    current_code = generated_code

    # ================================================
    # 5. TEST → EXECUTE → FIX LOOP
    # ================================================

    for attempt in range(max_attempts):

        result["attempts"] = attempt + 1

        # --------------------------------------------
        # TEST
        # --------------------------------------------

        test_result = test_python_file(
            main_file
        )

        result["test_passed"] = test_result["passed"]
        result["test_output"] = test_result["output"]
        result["test_error"] = test_result["error"]

        # --------------------------------------------
        # TEST PASSED
        # --------------------------------------------

        if test_result["passed"]:

            execution_result = run_python_file(
                main_file
            )

            # ----------------------------------------
            # EXECUTION PASSED
            # ----------------------------------------

            if execution_result["success"]:

                result["success"] = True
                result["output"] = execution_result["stdout"]
                result["error"] = ""

                save_task(
                    task,
                    "Completed"
                )

                return result

            # ----------------------------------------
            # EXECUTION FAILED
            # ----------------------------------------

            result["error"] = execution_result["stderr"]

        else:

            result["error"] = test_result["error"]

        # --------------------------------------------
        # NO MORE ATTEMPTS
        # --------------------------------------------

        if attempt == max_attempts - 1:

            save_task(
                task,
                "Failed After Fix"
            )

            return result

        # ============================================
        # 6. AI DEBUGGING
        # ============================================

        try:

            fixed_code = fix_python_project(
                task,
                current_code,
                result["error"]
            )

            current_code = fixed_code

        except Exception as error:

            result["error"] = str(error)

            save_task(
                task,
                "Debugging Failed"
            )

            return result

        # ============================================
        # 7. CREATE FIXED FILES
        # ============================================

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

        # ============================================
        # 8. FIND MAIN FILE AGAIN
        # ============================================

        main_file = Path("workspace/main.py")

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
                    "No Python file was found after fixing."
                )

                save_task(
                    task,
                    "No Python File After Fix"
                )

                return result

    return result