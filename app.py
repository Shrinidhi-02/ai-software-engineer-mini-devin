import streamlit as st

from agent import run_agent
from database import create_tables
from analytics import get_task_dataframe, create_status_chart


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Mini Devin",
    layout="wide"
)


# --------------------------------------------------
# Database
# --------------------------------------------------

create_tables()


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("AI Software Engineer - Mini Devin")

st.write(
    "Mini Devin analyzes software requirements, creates project plans, "
    "generates Python code, creates files, executes projects, "
    "and attempts to fix errors automatically."
)

st.divider()


# --------------------------------------------------
# Navigation
# --------------------------------------------------

page = st.sidebar.radio(
    "Navigation",
    [
        "Software Engineer",
        "Project History",
        "Analytics"
    ]
)


# ==================================================
# SOFTWARE ENGINEER
# ==================================================

if page == "Software Engineer":

    st.subheader("Software Development Requirement")

    task = st.text_area(
        "Describe the project you want to build:",
        placeholder=(
            "Example: Create a Python calculator application "
            "with addition, subtraction, multiplication and division."
        ),
        height=180
    )


    if st.button("Build Python Project"):

        if not task.strip():

            st.warning(
                "Please describe your project requirement."
            )

        else:

            with st.spinner(
                "Mini Devin is working on your project..."
            ):

                result = run_agent(task)


            # ------------------------------------------
            # Project Plan
            # ------------------------------------------

            if result["project_plan"]:

                st.success(
                    "Project plan created."
                )

                with st.expander(
                    "📋 View Project Plan"
                ):

                    st.markdown(
                        result["project_plan"]
                    )


            # ------------------------------------------
            # Generated Code
            # ------------------------------------------

            if result["generated_code"]:

                st.success(
                    "Python code generated."
                )

                with st.expander(
                    "View Generated Code"
                ):

                    st.markdown(
                        result["generated_code"]
                    )


            # ------------------------------------------
            # Created Files
            # ------------------------------------------

            if result["created_files"]:

                st.subheader(
                    "Created Files"
                )

                for file_path in result["created_files"]:

                    st.write(
                        f"`{file_path}`"
                    )


            # ------------------------------------------
            # Final Result
            # ------------------------------------------

            if result["success"]:

                st.success(
                    "🎉 Project completed successfully!"
                )

                st.write(
                    f"Execution attempts: {result['attempts']}"
                )

                if result["output"]:

                    st.subheader(
                        "📤 Output"
                    )

                    st.code(
                        result["output"]
                    )

                else:

                    st.info(
                        "The project executed successfully "
                        "but produced no console output."
                    )

            else:

                st.error(
                    "Mini Devin could not complete the project."
                )

                if result["error"]:

                    st.subheader(
                        "🐛 Error"
                    )

                    st.code(
                        result["error"]
                    )

                st.write(
                    f"Execution attempts: {result['attempts']}"
                )


# ==================================================
# PROJECT HISTORY
# ==================================================

elif page == "Project History":

    st.subheader(
        "Project History"
    )

    dataframe = get_task_dataframe()

    if dataframe.empty:

        st.info(
            "No project history available yet."
        )

    else:

        st.dataframe(
            dataframe,
            use_container_width=True
        )


# ==================================================
# ANALYTICS
# ==================================================

elif page == "Analytics":

    st.subheader(
        "Mini Devin Analytics"
    )

    dataframe = get_task_dataframe()

    if dataframe.empty:

        st.info(
            "No data available for analytics yet."
        )

    else:

        total_tasks = len(dataframe)

        completed_tasks = len(
            dataframe[
                dataframe["status"].isin(
                    [
                        "Completed",
                        "Fixed Successfully"
                    ]
                )
            ]
        )

        failed_tasks = len(
            dataframe[
                dataframe["status"].str.contains(
                    "Failed",
                    na=False
                )
            ]
        )


        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Total Tasks",
                total_tasks
            )

        with col2:

            st.metric(
                "Completed",
                completed_tasks
            )

        with col3:

            st.metric(
                "Failed",
                failed_tasks
            )


        st.divider()


        st.subheader(
            "Task Status Distribution"
        )

        chart = create_status_chart()

        if chart is not None:

            st.pyplot(chart)


        st.subheader(
            "Task Data"
        )

        st.dataframe(
            dataframe,
            use_container_width=True
        )


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "Mini Devin | AI Software Engineer"
)