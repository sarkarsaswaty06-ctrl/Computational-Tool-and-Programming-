import numpy as np
from scipy.optimize import minimize

# Define the function
def f(x):
    return (x[0] - 2)**2 + (x[1] - 2)**2

# Initial guess
initial_guess = [0, 0]

# Perform optimization
result = minimize(f, initial_guess, method='BFGS')

# Display results
print("Optimization Result")
print("--------------------")
print("Optimal x =", result.x[0])
print("Optimal y =", result.x[1])
print("Minimum value =", result.fun)
print("Success =", result.success)
