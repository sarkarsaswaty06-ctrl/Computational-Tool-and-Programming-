import numpy as np
from scipy.optimize._numdiff import approx_derivative
from scipy.integrate import quad

# Define the mathematical function
def f(x):
    return x**3 + 2*x**2 + x

# Numerical differentiation
x = 2

def function_for_derivative(x_array):
    return np.array([f(x_array[0])])

derivative_value = approx_derivative(
    function_for_derivative,
    np.array([x])
)[0, 0]

print("Function: f(x) = x^3 + 2x^2 + x")
print("Numerical derivative at x =", x)
print("Derivative =", derivative_value)

# Numerical integration
lower_limit = 0
upper_limit = 2

integral, error = quad(f, lower_limit, upper_limit)

print("\nNumerical Integration")
print("Limits:", lower_limit, "to", upper_limit)
print("Integral =", integral)
print("Estimated error =", error)
