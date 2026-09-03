import subprocess
import sys
from pathlib import Path


def test_python_file(file_path, timeout=20):
    """
    Test a Python file and return the result.
    """

    file_path = Path(file_path)

    if not file_path.exists():
        return {
            "passed": False,
            "output": "",
            "error": f"File not found: {file_path}",
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
            "passed": result.returncode == 0,
            "output": result.stdout,
            "error": result.stderr,
            "return_code": result.returncode
        }

    except subprocess.TimeoutExpired:

        return {
            "passed": False,
            "output": "",
            "error": "Test timed out.",
            "return_code": -1
        }

    except Exception as error:

        return {
            "passed": False,
            "output": "",
            "error": str(error),
            "return_code": -1
        }