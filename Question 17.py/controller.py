class EmployeeController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    # CREATE
    def add_employee(self):

        employee_id, name, designation, department, salary = \
            self.view.get_employee_details()

        result = self.model.add_employee(
            employee_id,
            name,
            designation,
            department,
            salary
        )

        if result:
            self.view.show_message(
                "Employee added successfully!"
            )
        else:
            self.view.show_message(
                "Employee ID already exists."
            )

    # READ
    def display_employees(self):

        employees = self.model.get_all_employees()

        self.view.display_employees(employees)

    def search_employee(self):

        employee_id = self.view.get_employee_id()

        employee = self.model.get_employee(employee_id)

        self.view.display_employee(employee)

    # UPDATE
    def update_employee(self):

        employee_id = self.view.get_employee_id()

        employee = self.model.get_employee(employee_id)

        if not employee:
            self.view.show_message(
                "Employee not found."
            )
            return

        print("\nEnter New Employee Details")

        name = input("Enter Name: ")
        designation = input("Enter Designation: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        result = self.model.update_employee(
            employee_id,
            name,
            designation,
            department,
            salary
        )

        if result:
            self.view.show_message(
                "Employee updated successfully!"
            )

    # DELETE
    def delete_employee(self):

        employee_id = self.view.get_employee_id()

        result = self.model.delete_employee(employee_id)

        if result:
            self.view.show_message(
                "Employee deleted successfully!"
            )
        else:
            self.view.show_message(
                "Employee not found."
            )

    # APPLICATION LOOP
    def run(self):

        while True:

            self.view.display_menu()

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_employee()

            elif choice == "2":
                self.display_employees()

            elif choice == "3":
                self.search_employee()

            elif choice == "4":
                self.update_employee()

            elif choice == "5":
                self.delete_employee()

            elif choice == "6":
                self.view.show_message(
                    "Thank you for using the system!"
                )
                break

            else:
                self.view.show_message(
                    "Invalid choice. Please try again."
                )
