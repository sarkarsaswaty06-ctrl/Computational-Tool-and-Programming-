class StudentView:

    def display_menu(self):
        print("\n===== Student Information Management System =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

    def get_student_details(self):
        roll_no = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        cgpa = float(input("Enter CGPA: "))

        return roll_no, name, department, cgpa

    def display_students(self, students):
        if not students:
            print("\nNo student records found.")
            return

        print("\n" + "-" * 60)
        print(f"{'Roll No':<10}{'Name':<20}{'Department':<15}{'CGPA':<10}")
        print("-" * 60)

        for student in students:
            print(
                f"{student[0]:<10}"
                f"{student[1]:<20}"
                f"{student[2]:<15}"
                f"{student[3]:<10.2f}"
            )

        print("-" * 60)

    def display_student(self, student):
        if student:
            print("\nStudent Details")
            print("-------------------------")
            print(f"Roll Number : {student[0]}")
            print(f"Name        : {student[1]}")
            print(f"Department  : {student[2]}")
            print(f"CGPA        : {student[3]:.2f}")
        else:
            print("\nStudent not found.")

    def show_message(self, message):
        print(f"\n{message}")

    def get_roll_number(self):
        return int(input("Enter Roll Number: "))
