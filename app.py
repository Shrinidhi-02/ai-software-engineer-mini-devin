import streamlit as st

from planner import create_project_plan


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Mini Devin",
    layout="wide"
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("AI Software Engineer - Mini Devin")

st.write(
    "Mini Devin is an AI-powered software engineering "
    "assistant that analyzes software requirements "
    "and creates structured development plans."
)

st.divider()


# --------------------------------------------------
# Project Requirement
# --------------------------------------------------

st.subheader("Software Development Requirement")

task = st.text_area(
    "Describe the project you want to build:",
    placeholder=(
        "Example: Build a Python expense tracker "
        "that stores expenses, calculates monthly "
        "spending and displays charts."
    ),
    height=180
)


# --------------------------------------------------
# Project Planner
# --------------------------------------------------

if st.button("Create Project Plan"):

    if not task.strip():

        st.warning(
            "Please describe your project requirement."
        )

    else:

        st.subheader("Your Requirement")

        st.code(task)

        # Generate project plan
        with st.spinner(
            "Mini Devin is creating your project plan..."
        ):

            try:

                project_plan = create_project_plan(task)

                st.success(
                    "Project plan generated successfully!"
                )

                st.subheader(
                    "Mini Devin Project Plan"
                )

                st.markdown(project_plan)

            except Exception as error:

                st.error(
                    "Unable to generate the project plan."
                )

                st.code(str(error))


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "Mini Devin | AI Software Engineer"
)