# Program to analyse student course enrolments
#  Develop a Python program to analyse student course enrolments by using set operations (union, intersection, difference) to identify students enrolled in common and unique courses, and tuples to store student details.    

# Using sets and tuples

# Student details stored as tuples
student1 = ("101", "Rahul", "Computer Science")
student2 = ("102", "Priya", "Information Technology")

# Courses enrolled by each student
courses_student1 = {"Python", "Database", "Web Development", "Mathematics"}
courses_student2 = {"Python", "Database", "Networking", "Statistics"}

print("Student 1 Details:", student1)
print("Student 2 Details:", student2)

print("\nCourses of Student 1:", courses_student1)
print("Courses of Student 2:", courses_student2)

# Union - all unique courses
union_courses = courses_student1.union(courses_student2)
print("\nUnion of Courses:")
print(union_courses)

# Intersection - common courses
common_courses = courses_student1.intersection(courses_student2)
print("\nCommon Courses:")
print(common_courses)

# Difference - courses unique to Student 1
unique_student1 = courses_student1.difference(courses_student2)
print("\nCourses Unique to Student 1:")
print(unique_student1)

# Difference - courses unique to Student 2
unique_student2 = courses_student2.difference(courses_student1)
print("\nCourses Unique to Student 2:")
print(unique_student2)
