import streamlit as st

st.set_page_config(
    page_title="Mini Devin",
    layout="wide"
)

st.title(" AI Software Engineer - Mini Devin")

st.write(
    "Give the AI a software development task and "
    "let it plan, generate and test Python code."
)

task = st.text_area(
    "Enter your software development task:",
    placeholder="Example: Create a Python calculator application"
)

if st.button("Start AI Engineer"):
    if task.strip():
        st.success("Task received!")
        st.write("Your task:")
        st.code(task)
    else:
        st.warning("Please enter a task.")