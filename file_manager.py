from pathlib import Path
import re


def clean_code(code):
    """
    Remove Markdown code fences from AI-generated code.
    """

    code = code.strip()

    code = re.sub(
        r"^```python\s*",
        "",
        code,
        flags=re.IGNORECASE
    )

    code = re.sub(
        r"^```\s*",
        "",
        code
    )

    code = re.sub(
        r"\s*```$",
        "",
        code
    )

    return code.strip()


def create_project_files(generated_code, workspace="workspace"):
    """
    Create Python project files from AI-generated output.

    Supports:
    - main.py
    - multiple Python files
    - Markdown files
    - text files
    """

    workspace_path = Path(workspace)

    workspace_path.mkdir(
        parents=True,
        exist_ok=True
    )

    created_files = []

    # --------------------------------------------------
    # Case 1: AI returns multiple files
    # --------------------------------------------------

    file_blocks = re.findall(
        r"(?:FILE|File):\s*([^\n]+)\n(.*?)(?=(?:\n(?:FILE|File):\s*)|\Z)",
        generated_code,
        flags=re.DOTALL
    )

    if file_blocks:

        for filename, content in file_blocks:

            filename = filename.strip()

            # Remove Markdown formatting
            filename = filename.replace("`", "")

            # Prevent paths from escaping workspace
            filename = Path(filename).name

            file_path = workspace_path / filename

            file_path.write_text(
                clean_code(content),
                encoding="utf-8"
            )

            created_files.append(
                str(file_path)
            )

        return created_files


    # --------------------------------------------------
    # Case 2: AI returns normal Python code
    # --------------------------------------------------

    cleaned_code = clean_code(
        generated_code
    )

    main_file = workspace_path / "main.py"

    main_file.write_text(
        cleaned_code,
        encoding="utf-8"
    )

    created_files.append(
        str(main_file)
    )

    return created_files