import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Given data points
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([6, 17, 34, 57, 86, 121])

# Define a second-degree polynomial
def polynomial(x, a, b, c):
    return a * x**2 + b * x + c

# Fit the polynomial to the data
coefficients, covariance = curve_fit(polynomial, x, y)

# Extract coefficients
a, b, c = coefficients

# Display coefficients
print("Estimated Polynomial Coefficients:")
print("a =", a)
print("b =", b)
print("c =", c)

print("\nFitted Polynomial:")
print(f"y = {a:.2f}x² + {b:.2f}x + {c:.2f}")

# Generate points for the fitted curve
x_curve = np.linspace(min(x), max(x), 100)
y_curve = polynomial(x_curve, a, b, c)

# Plot original data points
plt.scatter(x, y, label="Original Data")

# Plot fitted curve
plt.plot(x_curve, y_curve, label="Fitted Curve")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Second-Degree Polynomial Curve Fitting")
plt.legend()
plt.grid(True)
plt.show()
