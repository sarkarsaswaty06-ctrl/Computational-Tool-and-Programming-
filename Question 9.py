import numpy as np

# Given data
marks = [78, 85, 92, 67, 88, 73, 95, 81, 76, 89]

temperatures = [28.5, 30.2, 29.8, 31.4, 27.9, 32.1, 30.5]

sales = [12500, 13800, 14200, 11900, 15100, 14750, 16000]


# Function to calculate statistical measures using NumPy
def calculate_statistics(data, name):
    arr = np.array(data)

    print("\n", name)
    print("-" * 30)
    print("Mean:", np.mean(arr))
    print("Median:", np.median(arr))
    print("Standard Deviation:", np.std(arr))
    print("Minimum:", np.min(arr))
    print("Maximum:", np.max(arr))


# Calculate statistics
calculate_statistics(marks, "Marks")
calculate_statistics(temperatures, "Temperatures")
calculate_statistics(sales, "Sales")
