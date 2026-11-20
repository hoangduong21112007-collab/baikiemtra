n = int(input("Enter the number of employees: "))

employees = []

for i in range(n):
    print(f"\nEnter information for employee {i + 1}:")

    emp_id = input("Employee ID: ")
    name = input("Full name: ")
    salary = float(input("Salary: "))

    employee = {
        "id": emp_id,
        "name": name,
        "salary": salary
    }

    employees.append(employee)

print("\ntất cả nhân viên:")

for emp in employees:
    print("ID:", emp["id"])
    print("Name:", emp["name"])
    print("Salary:", emp["salary"])
    print("--------------------")

if len(employees) > 0:
    highest_employee = max(employees, key=lambda x: x["salary"])

    print("\nNhân viên có mức lương cao nhất:")
    print("ID:", highest_employee["id"])
    print("Name:", highest_employee["name"])
    print("Salary:", highest_employee["salary"])

    total_salary = sum(emp["salary"] for emp in employees)
    average_salary = total_salary / n

    print("\nMức lương trung bình:", average_salary)

    print("\nCác nhân viên có mức lương lớn hơn 10.000:")

    for emp in employees:
        if emp["salary"] > 10000:
            print(emp)
