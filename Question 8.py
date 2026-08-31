import numpy as np

# Student names
students = np.array(["S1", "S2", "S3", "S4", "S5"])

# Mid-Semester marks
mid_sem = np.array([
    [65, 70, 68, 72],
    [78, 75, 80, 77],
    [55, 60, 58, 62],
    [82, 85, 80, 88],
    [70, 68, 72, 74]
])

# End-Semester marks
end_sem = np.array([
    [72, 78, 75, 80],
    [84, 82, 86, 83],
    [65, 68, 66, 70],
    [88, 90, 85, 92],
    [78, 75, 80, 82]
])

# Calculate total marks using vectorized operation
mid_total = np.sum(mid_sem, axis=1)
end_total = np.sum(end_sem, axis=1)

# Calculate average marks
mid_average = np.mean(mid_sem, axis=1)
end_average = np.mean(end_sem, axis=1)

# Calculate percentage improvement
percentage_improvement = ((end_total - mid_total) / mid_total) * 100

# Display results
print("Student Performance Analysis")
print("-" * 75)
print("Student  Mid Total  Mid Avg  End Total  End Avg  Improvement (%)")
print("-" * 75)

for i in range(len(students)):
    print(f"{students[i]:<8} {mid_total[i]:<10} "
          f"{mid_average[i]:<8.2f} {end_total[i]:<10} "
          f"{end_average[i]:<8.2f} {percentage_improvement[i]:.2f}")
