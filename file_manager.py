import os


def create_project_files(generated_code, project_folder="workspace"):
    """
    Create project files from AI-generated code.

    Expected format:

    FILE: filename.py

    CODE:
    code here

    END FILE
    """

    os.makedirs(project_folder, exist_ok=True)

    sections = generated_code.split("FILE:")

    created_files = []

    for section in sections[1:]:
        lines = section.strip().splitlines()

        if not lines:
            continue

        filename = lines[0].strip()

        if "CODE:" not in lines:
            continue

        code_start = lines.index("CODE:") + 1

        code_lines = []

        for line in lines[code_start:]:
            if line.strip() == "END FILE":
                break

            code_lines.append(line)

        code = "\n".join(code_lines).strip()

        if not filename or not code:
            continue

        file_path = os.path.join(project_folder, filename)

        parent_folder = os.path.dirname(file_path)

        if parent_folder:
            os.makedirs(parent_folder, exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(code + "\n")

        created_files.append(file_path)

    return created_files