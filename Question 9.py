import numpy as np

# Input data
data = [10, 20, 30, 40, 50, 60, 70]

# Convert list to NumPy array
arr = np.array(data)

# Calculate statistical measures
mean = np.mean(arr)
median = np.median(arr)
std_dev = np.std(arr)
minimum = np.min(arr)
maximum = np.max(arr)

# Display results
print("Data:", arr)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
print("Minimum:", minimum)
print("Maximum:", maximum)
