import streamlit as st
from pathlib import Path

from planner import create_project_plan
from code_generator import generate_python_project
from file_manager import create_project_files
from executor import run_python_file


st.set_page_config(
    page_title="Mini Devin",
    layout="wide"
)


st.title("AI Software Engineer - Mini Devin")

st.write(
    "Mini Devin analyzes requirements, creates project plans, "
    "generates Python code, creates files, and executes projects."
)

st.divider()


st.subheader("Software Development Requirement")

task = st.text_area(
    "Describe the project you want to build:",
    placeholder=(
        "Example: Create a Python calculator application "
        "with addition, subtraction, multiplication and division."
    ),
    height=180
)


if st.button("Build and Run Python Project"):

    if not task.strip():

        st.warning(
            "Please describe your project requirement."
        )

    else:

        # ------------------------------------------
        # Project Planning
        # ------------------------------------------

        with st.spinner("Creating project plan..."):

            try:

                project_plan = create_project_plan(task)

            except Exception as error:

                st.error(
                    "Unable to create the project plan."
                )

                st.code(str(error))

                st.stop()


        st.success(
            "Project plan created successfully!"
        )

        with st.expander("View Project Plan"):
            st.markdown(project_plan)


        # ------------------------------------------
        # Code Generation
        # ------------------------------------------

        with st.spinner("Generating Python project..."):

            try:

                generated_code = generate_python_project(
                    task,
                    project_plan
                )

            except Exception as error:

                st.error(
                    "Unable to generate the Python project."
                )

                st.code(str(error))

                st.stop()


        st.success(
            "Python project generated successfully!"
        )

        with st.expander("View Generated Code"):
            st.markdown(generated_code)


        # ------------------------------------------
        # File Creation
        # ------------------------------------------

        with st.spinner("Creating project files..."):

            try:

                created_files = create_project_files(
                    generated_code,
                    "workspace"
                )

            except Exception as error:

                st.error(
                    "Unable to create project files."
                )

                st.code(str(error))

                st.stop()


        if not created_files:

            st.warning(
                "No project files were created."
            )

            st.stop()


        st.success(
            "Project files created successfully!"
        )

        st.subheader("Created Files")

        for file_path in created_files:
            st.write(f"`{file_path}`")


        # ------------------------------------------
        # Find Entry File
        # ------------------------------------------

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
                st.warning(
                    "No Python file was found to execute."
                )

                st.stop()


        # ------------------------------------------
        # Execute Python Project
        # ------------------------------------------

        st.subheader("Execution Result")

        with st.spinner("Running generated Python code..."):

            execution_result = run_python_file(
                main_file
            )


        if execution_result["success"]:

            st.success(
                "Python project executed successfully!"
            )

            if execution_result["stdout"]:

                st.subheader("Output")

                st.code(
                    execution_result["stdout"]
                )

            else:

                st.info(
                    "The program finished successfully "
                    "but did not produce console output."
                )

        else:

            st.error(
                "The generated project produced an error."
            )

            st.subheader("Error")

            st.code(
                execution_result["stderr"]
            )

            st.write(
                "This error will later be sent back "
                "to the AI debugging module."
            )


st.divider()

st.caption(
    "Mini Devin | AI Software Engineer"
)