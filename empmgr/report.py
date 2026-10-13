
def department_summary(employees):
    summary = {}

    for employee in employees:
        department = employee["department"]
        salary = float(employee["salary"])

        if department not in summary:
            summary[department] = {
                "headcount": 0,
                "total_salary": 0
            }

        summary[department]["headcount"] += 1
        summary[department]["total_salary"] += salary

    for department in summary:
        count = summary[department]["headcount"]
        total = summary[department]["total_salary"]

        summary[department]["average_salary"] = total / count
        del summary[department]["total_salary"]

    return summary
