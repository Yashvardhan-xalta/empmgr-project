# Employee Data Manager

A Python command-line application for managing employee records, storing employee data in JSON, validating employee details, and generating department-wise reports.

## Features

- Employee data model
- JSON-based employee storage
- Employee management operations
- Command-line interface
- Salary and email validation
- Department-wise employee count and average salary report

## Setup Instructions

Run these commands in PowerShell from the project directory.

### 1. Create a virtual environment

```powershell
py -m venv .venv
```

### 2. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Run the application

```powershell
python -m empmgr.cli
```

## Usage

Follow the menu displayed in the terminal to manage employee records and access the available operations.

## Git History

Run `git log --oneline --graph --all` in the terminal to view the project’s commit history.