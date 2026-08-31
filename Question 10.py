import numpy as np

# Define two matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Matrix Addition
print("\nAddition (A + B):")
print(A + B)

# Matrix Subtraction
print("\nSubtraction (A - B):")
print(A - B)

# Matrix Multiplication
print("\nMultiplication (A x B):")
print(np.dot(A, B))

# Transpose
print("\nTranspose of A:")
print(A.T)

print("\nTranspose of B:")
print(B.T)
