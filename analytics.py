import pandas as pd
import matplotlib.pyplot as plt

from database import get_all_tasks


def get_task_dataframe():
    """
    Convert stored tasks into a Pandas DataFrame.
    """

    tasks = get_all_tasks()

    columns = [
        "id",
        "task",
        "status",
        "created_at"
    ]

    return pd.DataFrame(tasks, columns=columns)


def get_status_counts():
    """
    Count tasks by status.
    """

    dataframe = get_task_dataframe()

    if dataframe.empty:
        return pd.DataFrame(
            columns=["status", "count"]
        )

    status_counts = (
        dataframe["status"]
        .value_counts()
        .reset_index()
    )

    status_counts.columns = [
        "status",
        "count"
    ]

    return status_counts


def create_status_chart():
    """
    Create a Matplotlib chart showing
    task status distribution.
    """

    status_counts = get_status_counts()

    if status_counts.empty:
        return None

    figure = plt.figure(figsize=(8, 5))

    plt.bar(
        status_counts["status"],
        status_counts["count"]
    )

    plt.xlabel("Status")
    plt.ylabel("Number of Tasks")
    plt.title("Mini Devin Task Status")

    plt.tight_layout()

    return figure