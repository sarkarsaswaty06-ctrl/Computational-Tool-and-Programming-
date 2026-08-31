# Program to read student marks from a text file
# and write total, average and grade to an output file

def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# Open input and output files
with open("students.txt", "r") as input_file, \
     open("results.txt", "w") as output_file:

    # Write heading to output file
    output_file.write("Student Results\n")
    output_file.write("-" * 60 + "\n")

    # Read each student record
    for line in input_file:
        data = line.strip().split(",")

        roll_no = data[0]
        name = data[1]

        # Convert marks to integers
        marks = [int(mark) for mark in data[2:]]

        # Calculate total and average
        total = sum(marks)
        average = total / len(marks)

        # Calculate grade
        grade = calculate_grade(average)

        # Display on screen
        print("Roll Number:", roll_no)
        print("Name:", name)
        print("Total:", total)
        print("Average:", round(average, 2))
        print("Grade:", grade)
        print()

        # Write results to output file
        output_file.write(f"Roll Number: {roll_no}\n")
        output_file.write(f"Name: {name}\n")
        output_file.write(f"Marks: {marks}\n")
        output_file.write(f"Total: {total}\n")
        output_file.write(f"Average: {average:.2f}\n")
        output_file.write(f"Grade: {grade}\n")
        output_file.write("-" * 60 + "\n")

print("Results have been written to results.txt")
