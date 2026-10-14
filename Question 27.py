
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Student examination data
data = {
    "Student": ["S1", "S2", "S3", "S4", "S5",
                "S6", "S7", "S8", "S9", "S10"],

    "Mathematics": [78, 85, 67, 90, 73, 81, 69, 94, 76, 88],
    "Physics":     [72, 88, 70, 92, 75, 79, 68, 90, 74, 85],
    "Chemistry":   [75, 82, 65, 88, 78, 83, 72, 92, 79, 86],
    "English":     [80, 84, 72, 91, 76, 80, 70, 95, 77, 89]
}

df = pd.DataFrame(data)

# Display dataset
print("Student Examination Data:")
print(df.to_string(index=False))

subjects = [
    "Mathematics", "Physics", "Chemistry", "English"
]

# 1. Subject-wise score distributions
plt.figure(figsize=(9, 5))
sns.boxplot(data=df[subjects])
plt.title("Subject-wise Score Distributions")
plt.ylabel("Marks")
plt.show()

# 2. Pairwise relationships
sns.pairplot(df[subjects], diag_kind="hist")
plt.suptitle("Pairwise Relationships Between Subjects", y=1.02)
plt.show()

# 3. Correlation heatmap
correlation = df[subjects].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    fmt=".2f"
)

plt.title("Correlation Heatmap of Examination Scores")
plt.show()

# Average marks per subject
print("\nAverage Marks:")
print(df[subjects].mean().round(2))

# Subject with the highest average
averages = df[subjects].mean()
print("\nHighest Average Subject:", averages.idxmax())
print("Average Marks:", round(averages.max(), 2))
