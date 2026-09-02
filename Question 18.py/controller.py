class EmployeeController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def generate_report(self):

        department = self.view.get_department()

        employees = self.model.get_salary_report(
            department
        )

        self.view.display_salary_report(
            department,
            employees
        )

        if employees:
            summary = self.model.get_department_summary(
                department
            )

            self.view.display_summary(summary)

    def show_departments(self):

        departments = self.model.get_departments()

        self.view.display_departments(
            departments
        )

    def run(self):

        while True:

            self.view.display_menu()

            choice = input("Enter your choice: ")

            if choice == "1":
                self.generate_report()

            elif choice == "2":
                self.show_departments()

            elif choice == "3":
                self.view.show_message(
                    "Thank you for using the system!"
                )
                break

            else:
                self.view.show_message(
                    "Invalid choice. Please try again."
                )
