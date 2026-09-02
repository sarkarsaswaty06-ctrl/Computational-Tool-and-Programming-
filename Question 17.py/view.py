class EmployeeView:

    def display_menu(self):
        print("\n======================================")
        print("     EMPLOYEE MANAGEMENT SYSTEM")
        print("======================================")
        print("1. Add Employee")
        print("2. Display All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        print("======================================")

    def get_employee_details(self):
        employee_id = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        designation = input("Enter Designation: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        return employee_id, name, designation, department, salary

    def get_employee_id(self):
        return int(input("Enter Employee ID: "))

    def display_employees(self, employees):

        if not employees:
            print("\nNo employee records found.")
            return

        print("\n" + "-" * 90)
        print(
            f"{'ID':<10}"
            f"{'Name':<20}"
            f"{'Designation':<20}"
            f"{'Department':<15}"
            f"{'Salary':<15}"
        )
        print("-" * 90)

        for employee in employees:
            print(
                f"{employee[0]:<10}"
                f"{employee[1]:<20}"
                f"{employee[2]:<20}"
                f"{employee[3]:<15}"
                f"{employee[4]:<15.2f}"
            )

        print("-" * 90)

    def display_employee(self, employee):

        if employee:
            print("\nEmployee Details")
            print("-----------------------------")
            print(f"Employee ID : {employee[0]}")
            print(f"Name        : {employee[1]}")
            print(f"Designation : {employee[2]}")
            print(f"Department  : {employee[3]}")
            print(f"Salary      : {employee[4]:.2f}")
        else:
            print("\nEmployee not found.")

    def show_message(self, message):
        print(f"\n{message}")
