# AI Software Engineer — Mini Devin

Mini Devin is a Python-based AI software engineering assistant that helps transform software requirements into working Python projects.

The application uses AI to understand a user's requirement, create a development plan, generate Python code, create project files, execute projects, detect errors, debug code, improve the generated code, store task history, and provide project analytics.

## Project Objective

The objective of Mini Devin is to build an AI-assisted software engineering workflow that can automate common development tasks while keeping the system simple, understandable, and extensible.

## Key Features

* AI-powered software requirement analysis

* Automatic project planning

* Python code generation

* Automatic project file creation

* Python code execution

* Error detection and analysis

* AI-assisted debugging

* Iterative code improvement

* Task and execution history

* Project analytics and visualization

* Task testing

* Python-based web interface

* Automated project validation

* Error handling

* Project status tracking

## Technologies Used

### Programming

* Python

* Python DSA

### AI

* OpenAI API

* AI-assisted code generation

* AI-assisted debugging

### Web Application

* Streamlit

### Data and Analytics

* Pandas

* NumPy

* Matplotlib

### Database

* SQL

* SQLite

### Development Tools

* VS Code

* Jupyter Notebook

* Git

* GitHub

## Requirements and Important Setup

Before running Mini Devin, make sure all required Python dependencies are installed.

Install the required dependencies using:

```bash
pip install -r requirements.txt

If the project is using a virtual environment, activate the virtual environment before installing the dependencies.

Important Note

Mini Devin requires the necessary Python libraries for all features to work correctly.

The Analytics section uses Matplotlib. If Matplotlib is not installed, the application may show an error such as:

ModuleNotFoundError: No module named 'matplotlib'

If the required dependencies are not installed, some features may not work correctly.

AI API Requirement

Mini Devin uses an AI API for AI-powered features such as project planning, code generation, debugging, and code improvement.

Make sure the required API key is configured before using the AI features.

Running the Application

After installing the dependencies, start the application using:

streamlit run app.py

The application will then be available in the browser.

System Workflow
User Requirement

       ↓

Requirement Analysis

       ↓

Project Planning

       ↓

Python Code Generation

       ↓

Project File Creation

       ↓

Code Execution

       ↓

Error Detection

       ↓

AI Debugging

       ↓

Code Improvement

       ↓

Re-execution

       ↓

Testing

       ↓

Task History

       ↓

Analytics

       ↓

Final Result
Project Architecture
Mini Devin
│
├── User Interface
│       │
│       └── Streamlit
│
├── AI Engine
│       │
│       └── AI API
│
├── Planner
│       │
│       └── Project Plan
│
├── Code Generator
│       │
│       └── Python Project Code
│
├── File Manager
│       │
│       └── Project Files
│
├── Testing System
│       │
│       └── Automated Tests
│
├── Execution System
│       │
│       └── Python Execution
│
├── Database
│       │
│       └── SQLite
│
└── Analytics
        │
        └── Pandas + Matplotlib
Main Project Components
AI Engine

The AI engine communicates with the AI model and processes prompts for project planning, code generation, debugging, and code improvement.

Planner

The planner analyzes the software requirement and creates a structured development plan.

Code Generator

The code generator converts the project plan into Python source code and prepares the required project files.

File Manager

The file manager creates and stores the generated project files inside the workspace.

Testing System

The testing system automatically runs the generated unit tests and reports whether the tests passed or failed.

Execution System

The execution system runs the generated Python project and captures the output and errors.

Database

SQLite is used to store project and task information for history and analytics.

Analytics

Pandas and Matplotlib are used to process task information and display project analytics and status visualization.

Streamlit Interface

Streamlit provides the web interface where users can enter requirements, view project plans, inspect generated code, check testing results, and view project history and analytics.

Testing

Mini Devin supports automated testing of generated Python projects.

The testing workflow checks:

Whether required files were created
Whether Python code can be imported
Whether unit tests pass
Whether the project executes successfully
Whether errors can be detected
Whether the final project produces the expected result
Example Project

Mini Devin can receive a requirement such as:

Create a Python program that checks whether a number is even or odd.

The system can then:

Requirement
     ↓
Project Plan
     ↓
Python Code
     ↓
Project Files
     ↓
Automated Tests
     ↓
Project Execution
     ↓
Final Result
Project History

Mini Devin stores completed and failed tasks in the database.

The project history can be used to view:

Previous requirements
Project status
Execution attempts
Testing results
Generated project information
Analytics

The Analytics section provides information about project execution.

It can display:

Total tasks
Completed tasks
Failed tasks
Task status distribution
Project task data
Error Handling

Mini Devin detects errors during project execution and testing.

When an error occurs, the system can analyze the error and attempt to improve the generated code before executing the project again.

Development Workflow
Requirement
     ↓
Planning
     ↓
Code Generation
     ↓
File Creation
     ↓
Testing
     ↓
Execution
     ↓
Error Detection
     ↓
Debugging
     ↓
Code Improvement
     ↓
Re-execution
     ↓
History
     ↓
Analytics
Project Goal

The main goal of Mini Devin is to demonstrate how AI can assist with software engineering tasks by automating the process from a natural-language requirement to a tested and executable Python project.

Current Project Status

Mini Devin currently demonstrates:

Requirement processing
Project planning
Python code generation
File creation
Automated testing
Project execution
Task history
Analytics
Streamlit-based user interface