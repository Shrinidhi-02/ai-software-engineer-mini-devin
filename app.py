import streamlit as st

from planner import create_project_plan
from code_generator import generate_python_project
from file_manager import create_project_files


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Mini Devin",
    page_icon="🤖",
    layout="wide"
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🤖 AI Software Engineer - Mini Devin")

st.write(
    "Mini Devin is an AI-powered software engineering "
    "assistant that analyzes requirements, creates project "
    "plans, generates Python code, and creates project files."
)

st.divider()


# --------------------------------------------------
# User Requirement
# --------------------------------------------------

st.subheader("📝 Software Development Requirement")

task = st.text_area(
    "Describe the project you want to build:",
    placeholder=(
        "Example: Create a Python calculator application "
        "with addition, subtraction, multiplication and division."
    ),
    height=180
)


# --------------------------------------------------
# Build Project
# --------------------------------------------------

if st.button("🚀 Build Python Project"):

    if not task.strip():

        st.warning(
            "Please describe your project requirement."
        )

    else:

        # --------------------------------------------------
        # Project Planning
        # --------------------------------------------------

        with st.spinner(
            "🤖 Creating project plan..."
        ):

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

        with st.expander("📋 View Project Plan"):

            st.markdown(project_plan)


        # --------------------------------------------------
        # Code Generation
        # --------------------------------------------------

        with st.spinner(
            "🐍 Generating Python project..."
        ):

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


        # --------------------------------------------------
        # Display Generated Code
        # --------------------------------------------------

        with st.expander("🐍 View Generated Python Code"):

            st.markdown(generated_code)


        # --------------------------------------------------
        # Create Project Files
        # --------------------------------------------------

        with st.spinner(
            "📁 Creating project files..."
        ):

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


        # --------------------------------------------------
        # Display Created Files
        # --------------------------------------------------

        if created_files:

            st.success(
                "Project files created successfully!"
            )

            st.subheader("📁 Created Files")

            for file_path in created_files:

                st.write(
                    f"✅ `{file_path}`"
                )

        else:

            st.warning(
                "No project files were detected."
            )


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "Mini Devin | AI Software Engineer"
)