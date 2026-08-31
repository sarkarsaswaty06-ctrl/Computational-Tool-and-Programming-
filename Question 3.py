# Develop a Python program to manage student records using lists and dictionaries, supporting insertion, deletion, and search operations.
# Program to manage student records using lists and dictionaries

students = []

while True:
    print("\n--- Student Record Management ---")
    print("1. Insert Student")
    print("2. Delete Student")
    print("3. Search Student")
    print("4. Display All Students")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # Insert student
    if choice == 1:
        roll_no = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        student = {
            "roll_no": roll_no,
            "name": name,
            "marks": marks
        }

        students.append(student)
        print("Student record inserted successfully.")

    # Delete student
    elif choice == 2:
        roll_no = int(input("Enter Roll Number to delete: "))

        found = False

        for student in students:
            if student["roll_no"] == roll_no:
                students.remove(student)
                print("Student record deleted successfully.")
                found = True
                break

        if not found:
            print("Student record not found.")

    # Search student
    elif choice == 3:
        roll_no = int(input("Enter Roll Number to search: "))

        found = False

        for student in students:
            if student["roll_no"] == roll_no:
                print("Student Found!")
                print("Roll Number:", student["roll_no"])
                print("Name:", student["name"])
                print("Marks:", student["marks"])
                found = True
                break

        if not found:
            print("Student record not found.")

    # Display all students
    elif choice == 4:
        if len(students) == 0:
            print("No student records available.")
        else:
            print("\nStudent Records:")
            for student in students:
                print(student)

    # Exit
    elif choice == 5:
        print("Program terminated.")
        break

    else:
        print("Invalid choice. Please try again.")
