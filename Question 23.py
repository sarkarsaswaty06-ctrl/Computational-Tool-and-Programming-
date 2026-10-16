
import xml.etree.ElementTree as ET
import os

FILE_NAME = "students.xml"


# Generate an XML document if it does not exist
def generate_xml():
    if not os.path.exists(FILE_NAME):
        root = ET.Element("students")
        tree = ET.ElementTree(root)
        save_xml(tree)
        print("New XML document created.")


# Save XML with proper indentation
def save_xml(tree):
    ET.indent(tree, space="    ")
    tree.write(
        FILE_NAME,
        encoding="utf-8",
        xml_declaration=True
    )


# Read and display all student records
def display_students():
    tree = ET.parse(FILE_NAME)
    root = tree.getroot()

    print("\n--- Student Records ---")

    for student in root.findall("student"):
        print("\nStudent ID:", student.get("id"))

        for field in student:
            print(field.tag.capitalize() + ":", field.text)


# Add a new student
def add_student():
    tree = ET.parse(FILE_NAME)
    root = tree.getroot()

    student_id = input("Enter student ID: ").strip()

    if root.find(f"student[@id='{student_id}']") is not None:
        print("Student ID already exists.")
        return

    name = input("Enter name: ").strip()
    department = input("Enter department: ").strip()
    year = input("Enter year: ").strip()
    email = input("Enter email: ").strip()
    cgpa = input("Enter CGPA: ").strip()

    if not all([student_id, name, department, year, email, cgpa]):
        print("All fields are required.")
        return

    try:
        if int(year) < 1 or int(year) > 8:
            print("Year must be between 1 and 8.")
            return

        if not 0 <= float(cgpa) <= 10:
            print("CGPA must be between 0 and 10.")
            return
    except ValueError:
        print("Year and CGPA must be numeric.")
        return

    student = ET.SubElement(root, "student", id=student_id)
    ET.SubElement(student, "name").text = name
    ET.SubElement(student, "department").text = department
    ET.SubElement(student, "year").text = year
    ET.SubElement(student, "email").text = email
    ET.SubElement(student, "cgpa").text = cgpa

    save_xml(tree)
    print("Student added successfully.")


# Update an existing student
def update_student():
    tree = ET.parse(FILE_NAME)
    root = tree.getroot()

    student_id = input("Enter student ID to update: ").strip()
    student = root.find(f"student[@id='{student_id}']")

    if student is None:
        print("Student not found.")
        return

    print("Leave a field blank to keep its current value.")

    for field in ["name", "department", "year", "email", "cgpa"]:
        element = student.find(field)
        new_value = input(
            f"Enter new {field} [{element.text}]: "
        ).strip()

        if new_value:
            if field == "year":
                try:
                    if not 1 <= int(new_value) <= 8:
                        print("Invalid year. Keeping old value.")
                        continue
                except ValueError:
                    print("Invalid year. Keeping old value.")
                    continue

            if field == "cgpa":
                try:
                    if not 0 <= float(new_value) <= 10:
                        print("Invalid CGPA. Keeping old value.")
                        continue
                except ValueError:
                    print("Invalid CGPA. Keeping old value.")
                    continue

            element.text = new_value

    save_xml(tree)
    print("Student updated successfully.")


# Delete a student
def delete_student():
    tree = ET.parse(FILE_NAME)
    root = tree.getroot()

    student_id = input("Enter student ID to delete: ").strip()
    student = root.find(f"student[@id='{student_id}']")

    if student is None:
        print("Student not found.")
        return

    root.remove(student)
    save_xml(tree)
    print("Student deleted successfully.")


# Main menu
def main():
    generate_xml()

    while True:
        print("\n===== Student Information Management =====")
        print("1. Display Students")
        print("2. Add Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                display_students()
            elif choice == "2":
                add_student()
            elif choice == "3":
                update_student()
            elif choice == "4":
                delete_student()
            elif choice == "5":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Try again.")

        except ET.ParseError:
            print("Error: XML document is not valid.")
        except OSError as error:
            print("File error:", error)


if __name__ == "__main__":
    main()
