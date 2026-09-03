"""
Mini Devin - File Manager

Creates project files from generated AI/project code.
"""

from pathlib import Path
import re


def clean_code(code):
    """
    Remove Markdown code fences and END FILE markers
    from generated code.
    """

    code = code.strip()

    # Remove Markdown code fences
    code = re.sub(
        r"^```(?:python)?\s*",
        "",
        code,
        flags=re.IGNORECASE
    )

    code = re.sub(
        r"\s*```$",
        "",
        code
    )

    # Remove accidental END FILE markers
    code = re.sub(
        r"^\s*END FILE\s*$",
        "",
        code,
        flags=re.MULTILINE
    )

    return code.strip()


def create_project_files(
    generated_code,
    workspace="workspace"
):
    """
    Create project files from generated code.

    Expected format:

    FILE: filename.py

    CODE:
    Python code

    END FILE
    """

    workspace_path = Path(workspace)

    workspace_path.mkdir(
        parents=True,
        exist_ok=True
    )

    created_files = []

    # --------------------------------------------------
    # Make sure generated_code is text
    # --------------------------------------------------

    if not isinstance(generated_code, str):
        raise TypeError(
            "generated_code must be a string."
        )

    # --------------------------------------------------
    # Extract FILE / CODE / END FILE blocks
    # --------------------------------------------------

    pattern = (
        r"FILE:\s*(.+?)\s*\n"
        r"CODE:\s*\n"
        r"(.*?)"
        r"\nEND FILE"
    )

    file_blocks = re.findall(
        pattern,
        generated_code,
        flags=re.DOTALL | re.IGNORECASE
    )

    # --------------------------------------------------
    # Multiple files found
    # --------------------------------------------------

    if file_blocks:

        for filename, content in file_blocks:

            filename = filename.strip()

            # Remove Markdown backticks
            filename = filename.replace("`", "")

            # Keep only the filename
            filename = Path(filename).name

            # Skip empty filenames
            if not filename:
                continue

            file_path = (
                workspace_path / filename
            )

            cleaned_content = clean_code(
                content
            )

            file_path.write_text(
                cleaned_content,
                encoding="utf-8"
            )

            created_files.append(
                str(file_path)
            )

        return created_files

    # --------------------------------------------------
    # No FILE blocks
    # --------------------------------------------------

    cleaned_code = clean_code(
        generated_code
    )

    main_file = (
        workspace_path / "main.py"
    )

    main_file.write_text(
        cleaned_code,
        encoding="utf-8"
    )

    created_files.append(
        str(main_file)
    )

    return created_files