
import matplotlib.pyplot as plt

# Student data
students = ["S1", "S2", "S3", "S4", "S5",
            "S6", "S7", "S8", "S9", "S10"]

study_hours = [8, 10, 12, 15, 18, 20, 7, 14, 16, 22]
exam_scores = [65, 72, 75, 82, 88, 90, 60, 80, 85, 95]

plt.figure(figsize=(12, 5))

# Histogram of study hours
plt.subplot(1, 2, 1)
plt.hist(study_hours, bins=5, edgecolor="black")
plt.title("Distribution of Study Hours")
plt.xlabel("Study Hours per Week")
plt.ylabel("Number of Students")

# Scatter plot of study hours and scores
plt.subplot(1, 2, 2)
plt.scatter(study_hours, exam_scores)

plt.title("Study Hours vs Examination Scores")
plt.xlabel("Study Hours per Week")
plt.ylabel("Exam Score")

# Label each student
for i, student in enumerate(students):
    plt.annotate(
        student,
        (study_hours[i], exam_scores[i]),
        xytext=(4, 4),
        textcoords="offset points"
    )

plt.tight_layout()
plt.show()

# Identify highest and lowest scores
print("Highest Score:", max(exam_scores))
print("Lowest Score:", min(exam_scores))
