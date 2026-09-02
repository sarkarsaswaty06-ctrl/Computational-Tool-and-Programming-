class StudentController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_student(self):
        roll_no, name, department, cgpa = self.view.get_student_details()

        if self.model.add_student(roll_no, name, department, cgpa):
            self.view.show_message("Student added successfully!")
        else:
            self.view.show_message(
                "Error: Roll number already exists."
            )

    def display_students(self):
        students = self.model.get_all_students()
        self.view.display_students(students)

    def search_student(self):
        roll_no = self.view.get_roll_number()
        student = self.model.get_student(roll_no)

        self.view.display_student(student)

    def update_student(self):
        roll_no = self.view.get_roll_number()

        student = self.model.get_student(roll_no)

        if not student:
            self.view.show_message("Student not found.")
            return

        print("\nEnter new student details:")
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        cgpa = float(input("Enter CGPA: "))

        if self.model.update_student(
            roll_no, name, department, cgpa
        ):
            self.view.show_message(
                "Student details updated successfully!"
            )

    def delete_student(self):
        roll_no = self.view.get_roll_number()

        if self.model.delete_student(roll_no):
            self.view.show_message(
                "Student deleted successfully!"
            )
        else:
            self.view.show_message("Student not found.")

    def run(self):
        while True:
            self.view.display_menu()

            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.display_students()

            elif choice == "3":
                self.search_student()

            elif choice == "4":
                self.update_student()

            elif choice == "5":
                self.delete_student()

            elif choice == "6":
                self.view.show_message(
                    "Thank you for using the system!"
                )
                break

            else:
                self.view.show_message(
                    "Invalid choice. Please try again."
                )
