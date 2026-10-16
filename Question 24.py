
import pandas as pd

#  Load the dataset
df = pd.read_csv("titanic.csv")

print("Original Dataset Shape:", df.shape)

# Display initial information
print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

print("\nDuplicate Rows Before Cleaning:", df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

#  Handle missing values
# Fill Age and Fare with their median values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Fare"] = df["Fare"].fillna(df["Fare"].median())

# Fill Embarked with its most frequent value
df["Embarked"] = df["Embarked"].fillna(
    df["Embarked"].mode()[0]
)

# Fill missing text values
df["Name"] = df["Name"].fillna("Unknown")
df["Ticket"] = df["Ticket"].fillna("Unknown")
df["Cabin"] = df["Cabin"].fillna("Unknown")

# Standardize text data
df["Sex"] = df["Sex"].str.strip().str.lower()
df["Embarked"] = df["Embarked"].str.strip().str.upper()

# Convert columns to appropriate data types
df["PassengerId"] = pd.to_numeric(
    df["PassengerId"], errors="coerce"
).astype("Int64")

df["Survived"] = pd.to_numeric(
    df["Survived"], errors="coerce"
).astype("Int64")

df["Pclass"] = pd.to_numeric(
    df["Pclass"], errors="coerce"
).astype("Int64")

df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Fare"] = pd.to_numeric(df["Fare"], errors="coerce")

# Check for remaining missing values
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Display cleaned data
print("\nCleaned Dataset:")
print(df.head())

print("\nCleaned Dataset Shape:", df.shape)

# Save the cleaned dataset
df.to_csv("titanic_cleaned.csv", index=False)

print("\nCleaned dataset saved as titanic_cleaned.csv")
