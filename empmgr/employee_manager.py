# employee_manager.py — single-file starter (copy as is) 
import json 
  
DATA_FILE = "employees.json" 
  
def load_employees(): 
    try: 
        with open(DATA_FILE, encoding="utf-8") as f: 
            return json.load(f) 
    except FileNotFoundError: 
        return [] 
  
def save_employees(employees): 
    with open(DATA_FILE, "w", encoding="utf-8") as f: 
        json.dump(employees, f, indent=2) 
  
def parse_salary(text): 
    try: 
        return float(text) 
    except ValueError: 
        return None 
  
def add_employee(employees, name, email, department, salary): 
    next_id = max((e["id"] for e in employees), default=0) + 1 
    employees.append({"id": next_id, "name": name, "email": email, 
                      "department": department, "salary": salary}) 
  
def main(): 
    employees = load_employees() 
    while True: 
        print("\n=== Employee Manager ===") 
        print("1. List employees") 
        print("2. Add employee") 
        print("3. Quit") 
        choice = input("Choose an option: ").strip() 
        if choice == "1": 
            for e in employees: 
                print(e["id"], e["name"], e["department"], e["salary"]) 
        elif choice == "2": 
            name = input("Name: ").strip() 
            email = input("Email: ").strip() 
            department = input("Department: ").strip() 
            salary = parse_salary(input("Salary: ")) 
            if not name or salary is None: 
                print("Invalid input - employee not added.") 
                continue 
            add_employee(employees, name, email, department, salary) 
            save_employees(employees) 
        elif choice == "3": 
            break 
        else: 
            print("Invalid option.") 

main()