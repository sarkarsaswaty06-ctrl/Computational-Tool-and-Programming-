import numpy as np

# Define the matrix
A = np.array([
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
])

print("Matrix A:")
print(A)

# Calculate determinant
determinant = np.linalg.det(A)

# Calculate inverse
if determinant != 0:
    inverse = np.linalg.inv(A)
else:
    inverse = None

# Calculate rank
rank = np.linalg.matrix_rank(A)

# Display results
print("\nDeterminant:")
print(round(determinant, 2))

if inverse is not None:
    print("\nInverse:")
    print(inverse)
else:
    print("\nInverse does not exist because the determinant is zero.")

print("\nRank:")
print(rank)
