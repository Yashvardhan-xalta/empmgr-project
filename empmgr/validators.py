
import re


def parse_salary(text):
    try:
        salary = float(text)

        if salary < 0:
            return None

        return salary
    except ValueError:
        return None


def is_valid_email(email):
    pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
    return re.match(pattern, email) is not None


def validate_employee(employee):
    salary = parse_salary(str(employee.get("salary", "")))
    email = employee.get("email", "")

    if salary is None:
        raise ValueError("Salary must be a valid non-negative number")

    if not is_valid_email(email):
        raise ValueError("Please enter a valid email address")

    return True
