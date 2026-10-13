\# Employee Data Manager

Setup and Run (Windows)

Follow these steps in PowerShell to set up and run the Employee Manager application.

1. Navigate to the project directory
cd "$HOME\Desktop\Training\Python Bootcamp\Day 6\Task 1 — Package structure\empmgr-project"

2. Create a virtual environment
py -m venv .venv

3. Activate the virtual environment
.\.venv\Scripts\Activate.ps1


If PowerShell blocks script execution, run:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned


Then activate the environment again.

4. Install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

5. Run the application
python -m empmgr.cli

6. Use the application
Enter 1 to list employees.
Enter 2 to add an employee.
Enter 3 to quit and display the employee table.
7. Deactivate the virtual environment
deactivate



A Python application for managing employee records.



\## Features



\- Employee data model

\- JSON-based employee storage

\- Employee management operations

\- Command-line interface

\- Salary and email validation

\- Department-wise headcount and average salary report



\## History



```text

\*   0142b78 (HEAD -> main) Merge validation feature

|\\  

| \* 67bfd2a (feature/validation) Add salary and email validation

\* |   9b04d97 Merge department reporting feature

|\\ \\  

| |/  

|/|   

| \* 5863d3d (feature/report) Add department summary report

|/  

\* 34bfe6e Add project dependencies

\* fa13916 Add employee command line interface

\* d721d86 Add employee management operations

\* d758285 Add JSON employee storage

\* 284d501 Add employee data model

\* 4c85e1c Add Python project gitignore

```

