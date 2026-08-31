import numpy as np
from scipy.misc import derivative
from scipy.integrate import quad

# Define the mathematical function
def f(x):
    return x**3 + 2*x**2 + x

# Point at which differentiation is required
x = 2

# Numerical differentiation
first_derivative = derivative(f, x, dx=1e-6)

print("Function: f(x) = x^3 + 2x^2 + x")
print("Point x =", x)
print("Numerical derivative at x =", first_derivative)

# Numerical integration
lower_limit = 0
upper_limit = 2

integral, error = quad(f, lower_limit, upper_limit)

print("\nNumerical Integration")
print("Limits:", lower_limit, "to", upper_limit)
print("Integral =", integral)
print("Estimated error =", error)
