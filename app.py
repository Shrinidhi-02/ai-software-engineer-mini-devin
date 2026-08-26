import streamlit as st

from ai_engine import ask_ai

st.set_page_config(
    page_title="Mini Devin",
    layout="wide"
)

st.title("AI Software Engineer - Mini Devin")

st.write(
    "Mini Devin is an AI-powered software engineering "
    "assistant that helps analyze software development tasks."
)

st.divider()

st.subheader("Software Development Task")

task = st.text_area(
    "Enter your task:",
    placeholder=(
        "Example: Create a Python calculator application "
        "with addition, subtraction, multiplication and division."
    ),
    height=150
)

if st.button("Ask Mini Devin"):

    if not task.strip():

        st.warning(
            "Please enter a software development task."
        )

    else:

        st.subheader("Your Task")

        st.code(task)

        prompt = f"""
You are Mini Devin, an AI Software Engineer.

The user has provided this software development task:

{task}

Analyze the requirement and provide:

1. A clear understanding of the requirement.
2. A simple development plan.
3. Python libraries that may be useful.
4. The files that may be required.
5. A simple explanation of how the project can be implemented.

Use Python only.

Do not use JavaScript, HTML or CSS.

Keep the explanation beginner-friendly.
"""

        with st.spinner(
            "Mini Devin is thinking..."
        ):

            try:

                response = ask_ai(prompt)

                st.success(
                    "AI response generated successfully!"
                )

                st.subheader(
                    "Mini Devin Response"
                )

                st.write(response)

            except Exception as error:

                st.error(
                    "Unable to connect to the AI."
                )

                st.code(str(error))

st.divider()

st.caption(
    "Mini Devin | AI Software Engineer"
)