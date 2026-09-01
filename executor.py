import subprocess
import sys
from pathlib import Path


def run_python_file(file_path, timeout=20):
    """
    Run a Python file and capture output and errors.
    """

    file_path = Path(file_path)

    if not file_path.exists():
        return {
            "success": False,
            "stdout": "",
            "stderr": f"File not found: {file_path}",
            "return_code": -1
        }

    try:
        result = subprocess.run(
            [sys.executable, file_path.name],
            cwd=file_path.parent,
            capture_output=True,
            text=True,
            timeout=timeout
        )

        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "return_code": result.returncode
        }

    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "stdout": "",
            "stderr": "Execution timed out.",
            "return_code": -1
        }

    except Exception as error:
        return {
            "success": False,
            "stdout": "",
            "stderr": str(error),
            "return_code": -1
        }