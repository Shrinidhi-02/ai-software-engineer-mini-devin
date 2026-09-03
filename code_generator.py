"""
Mini Devin - Code Generator
"""

import json


def generate_python_project(task, project_plan):
    """
    Generate project files based on the user's requirement.
    """

    task_lower = task.lower()

    # ==================================================
    # EVEN / ODD PROJECT
    # ==================================================

    if "even" in task_lower and "odd" in task_lower:

        main_code = '''def check_even_odd(number):
    """Check whether a number is even or odd."""
    if number % 2 == 0:
        return "Even"
    return "Odd"


def main():
    print("Even or Odd Checker")

    try:
        number = int(input("Enter a number: "))
        result = check_even_odd(number)
        print("Result:", result)

    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
'''

        test_code = '''import unittest

from main import check_even_odd


class TestEvenOdd(unittest.TestCase):

    def test_even_number(self):
        self.assertEqual(check_even_odd(10), "Even")

    def test_odd_number(self):
        self.assertEqual(check_even_odd(7), "Odd")

    def test_zero(self):
        self.assertEqual(check_even_odd(0), "Even")

    def test_negative_even(self):
        self.assertEqual(check_even_odd(-4), "Even")

    def test_negative_odd(self):
        self.assertEqual(check_even_odd(-3), "Odd")


if __name__ == "__main__":
    unittest.main()
'''

        readme_code = (
            "# Even or Odd Number Checker\n\n"
            "A simple Python program that checks whether a number "
            "is even or odd.\n\n"
            "## Features\n\n"
            "- Checks even numbers\n"
            "- Checks odd numbers\n"
            "- Handles zero\n"
            "- Handles negative numbers\n"
            "- Automated unit tests\n\n"
            "## Run\n\n"
            "python main.py\n\n"
            "## Test\n\n"
            "python -m unittest test_even_odd.py\n"
        )

        return (
            "FILE: main.py\n\n"
            "CODE:\n"
            + main_code
            + "\nEND FILE\n\n"
            "FILE: test_even_odd.py\n\n"
            "CODE:\n"
            + test_code
            + "\nEND FILE\n\n"
            "FILE: README.md\n\n"
            "CODE:\n"
            + readme_code
            + "\nEND FILE\n"
        )

    # ==================================================
    # CALCULATOR PROJECT
    # ==================================================

    if "calculator" in task_lower:

        calculator_code = '''def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return the result of dividing a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def calculate(a, operator, b):
    """Perform a calculation."""

    if operator == "+":
        return add(a, b)

    if operator == "-":
        return subtract(a, b)

    if operator == "*":
        return multiply(a, b)

    if operator == "/":
        return divide(a, b)

    raise ValueError("Invalid operator.")
'''

        main_code = '''from calculator import calculate


def main():
    print("Mini Devin Calculator")

    try:
        first_number = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        second_number = float(input("Enter second number: "))

        result = calculate(
            first_number,
            operator,
            second_number
        )

        print("Result:", result)

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
'''

        test_code = '''import unittest

from calculator import (
    add,
    subtract,
    multiply,
    divide,
    calculate
)


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(10, 5), 15)

    def test_subtraction(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiplication(self):
        self.assertEqual(multiply(10, 5), 50)

    def test_division(self):
        self.assertEqual(divide(10, 5), 2)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            calculate(10, "%", 5)


if __name__ == "__main__":
    unittest.main()
'''

        readme_code = (
            "# Mini Devin Calculator\n\n"
            "A simple Python calculator project.\n\n"
            "## Features\n\n"
            "- Addition\n"
            "- Subtraction\n"
            "- Multiplication\n"
            "- Division\n"
            "- Division by zero handling\n"
            "- Invalid operator handling\n"
            "- Automated unit tests\n\n"
            "## Run\n\n"
            "python main.py\n\n"
            "## Test\n\n"
            "python -m unittest test_calculator.py\n"
        )

        return (
            "FILE: calculator.py\n\n"
            "CODE:\n"
            + calculator_code
            + "\nEND FILE\n\n"
            "FILE: main.py\n\n"
            "CODE:\n"
            + main_code
            + "\nEND FILE\n\n"
            "FILE: test_calculator.py\n\n"
            "CODE:\n"
            + test_code
            + "\nEND FILE\n\n"
            "FILE: README.md\n\n"
            "CODE:\n"
            + readme_code
            + "\nEND FILE\n"
        )

    # ==================================================
    # DEFAULT PROJECT
    # ==================================================

    safe_task = json.dumps(task)

    main_code = (
        "def main():\n"
        "    print(\"Mini Devin Project\")\n"
        "    print(\"Requirement:\", " + safe_task + ")\n\n"
        "\n"
        "if __name__ == \"__main__\":\n"
        "    main()\n"
    )

    test_code = '''import unittest

from main import main


class TestProject(unittest.TestCase):

    def test_main_exists(self):
        self.assertTrue(callable(main))


if __name__ == "__main__":
    unittest.main()
'''

    readme_code = (
        "# Mini Devin Python Project\n\n"
        "This project was created by Mini Devin.\n\n"
        "## Requirement\n\n"
        + task
        + "\n\n"
        "## Run\n\n"
        "python main.py\n\n"
        "## Test\n\n"
        "python -m unittest discover\n"
    )

    return (
        "FILE: main.py\n\n"
        "CODE:\n"
        + main_code
        + "\nEND FILE\n\n"
        "FILE: test_project.py\n\n"
        "CODE:\n"
        + test_code
        + "\nEND FILE\n\n"
        "FILE: README.md\n\n"
        "CODE:\n"
        + readme_code
        + "\nEND FILE\n"
    )