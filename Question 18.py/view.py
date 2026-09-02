class EmployeeView:

    def display_menu(self):
        print("\n======================================")
        print("   DEPARTMENT-WISE SALARY REPORT")
        print("======================================")
        print("1. Generate Salary Report")
        print("2. Show Available Departments")
        print("3. Exit")
        print("======================================")

    def get_department(self):
        return input("Enter Department Name: ")

    def display_departments(self, departments):

        if not departments:
            print("\nNo departments found.")
            return

        print("\nAvailable Departments:")
        print("----------------------")

        for department in departments:
            print(department)

    def display_salary_report(self, department, employees):

        print("\n======================================")
        print(f"Salary Report - {department}")
        print("======================================")

        if not employees:
            print("No employees found in this department.")
            return

        print(
            f"{'ID':<10}"
            f"{'Name':<20}"
            f"{'Designation':<20}"
            f"{'Salary':<15}"
        )

        print("-" * 65)

        for employee in employees:
            print(
                f"{employee[0]:<10}"
                f"{employee[1]:<20}"
                f"{employee[2]:<20}"
                f"{employee[3]:<15.2f}"
            )

        print("-" * 65)

    def display_summary(self, summary):

        count, total, average, minimum, maximum = summary

        print("\nDepartment Salary Summary")
        print("--------------------------")
        print(f"Number of Employees : {count}")
        print(f"Total Salary        : {total:.2f}")
        print(f"Average Salary      : {average:.2f}")
        print(f"Minimum Salary      : {minimum:.2f}")
        print(f"Maximum Salary      : {maximum:.2f}")

    def show_message(self, message):
        print(f"\n{message}")
