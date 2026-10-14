
import xml.etree.ElementTree as ET

# Load and parse the XML document
tree = ET.parse("university_records.xml")
root = tree.getroot()

# Display university details
print("UNIVERSITY INFORMATION")
print("-" * 40)
print("University Name:", root.get("name"))

campus = root.find("campus")
print("Location:", campus.findtext("location"))
print("Established:", campus.findtext("established"))
print("Website:", campus.findtext("website"))

# Display department and student details
for department in root.findall("./departments/department"):
    print("\nDEPARTMENT:", department.findtext("name"))
    print("Department ID:", department.get("id"))
    print("HOD:", department.findtext("hod"))
    print("Building:", department.findtext("building"))

    for student in department.findall("./students/student"):
        personal = student.find("personal_details")
        academic = student.find("academic_details")

        first = personal.findtext("name/first_name")
        last = personal.findtext("name/last_name")
        full_name = f"{first} {last}"

        print("\n  Student ID:", student.get("id"))
        print("  Name:", full_name)
        print("  Email:", personal.findtext("email"))
        print("  Year:", academic.findtext("year"))
        print("  Semester:", academic.findtext("semester"))
        print("  CGPA:", academic.findtext("cgpa"))

        print("  Courses:")
        for course in academic.findall("./courses/course"):
            print(
                "   ",
                course.get("code"),
                "-",
                course.findtext("name"),
                "| Marks:", course.findtext("marks"),
                "| Grade:", course.findtext("grade")
            )
