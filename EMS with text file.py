# Employee Management System using Classes

class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def to_line(self):
        return f"{self.emp_id},{self.name},{self.department},{self.salary}\n"


def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    salary = input("Enter Salary: ")

    emp = Employee(emp_id, name, department, salary)

    with open("employees.txt", "a") as file:
        file.write(emp.to_line())

    print("✅ Employee added successfully.\n")


def view_all_employees():
    try:
        with open("employees.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No employee records found.\n")
                return

            print("\nEmployee Records:")
            print("ID\tName\tDepartment\tSalary")
            print("-" * 40)
            for line in lines:
                emp_id, name, department, salary = line.strip().split(",")
                print(f"{emp_id}\t{name}\t{department}\t{salary}")
            print()
    except FileNotFoundError:
        print("❌ Employee file not found.\n")


def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    found = False

    try:
        with open("employees.txt", "r") as file:
            for line in file:
                id_, name, department, salary = line.strip().split(",")
                if id_ == emp_id:
                    print(f"\nRecord Found:\nID: {id_}, Name: {name}, Department: {department}, Salary: {salary}\n")
                    found = True
                    break

        if not found:
            print("❌ Employee not found.\n")
    except FileNotFoundError:
        print("❌ Employee file not found.\n")


def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    updated = False
    new_lines = []

    try:
        with open("employees.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            id_, name, department, salary = line.strip().split(",")
            if id_ == emp_id:
                print(f"Current Record: {id_}, {name}, {department}, {salary}")
                name = input("Enter new name: ")
                department = input("Enter new department: ")
                salary = input("Enter new salary: ")
                emp = Employee(emp_id, name, department, salary)
                new_lines.append(emp.to_line())
                updated = True
            else:
                new_lines.append(line)

        with open("employees.txt", "w") as file:
            file.writelines(new_lines)

        if updated:
            print("✅ Employee updated successfully.\n")
        else:
            print("❌ Employee not found.\n")

    except FileNotFoundError:
        print("❌ Employee file not found.\n")


def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    deleted = False
    new_lines = []

    try:
        with open("employees.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            id_, *_ = line.strip().split(",")
            if id_ == emp_id:
                deleted = True
                continue
            new_lines.append(line)

        with open("employees.txt", "w") as file:
            file.writelines(new_lines)

        if deleted:
            print("✅ Employee deleted successfully.\n")
        else:
            print("❌ Employee not found.\n")

    except FileNotFoundError:
        print("❌ Employee file not found.\n")


def main_menu():
    while True:
        print("========= Employee Management System =========")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_all_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            update_employee()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            print("Exiting Employee Management System. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select between 1 to 6.\n")


# Run the EMS
main_menu()
