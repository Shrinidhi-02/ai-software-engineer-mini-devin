import sqlite3
from datetime import datetime


DATABASE_NAME = "mini_devin.db"


def get_connection():
    """
    Create a connection to the SQLite database.
    """
    return sqlite3.connect(DATABASE_NAME)


def create_tables():
    """
    Create the tasks table if it does not exist.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
        """
    )

    connection.commit()
    connection.close()


def save_task(task, status):
    """
    Save a software development task.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO tasks (task, status, created_at)
        VALUES (?, ?, ?)
        """,
        (
            task,
            status,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
    )

    connection.commit()
    connection.close()


def get_all_tasks():
    """
    Retrieve all stored tasks.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, task, status, created_at
        FROM tasks
        ORDER BY id DESC
        """
    )

    tasks = cursor.fetchall()

    connection.close()

    return tasks