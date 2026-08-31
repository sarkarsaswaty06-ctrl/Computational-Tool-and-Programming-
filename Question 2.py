# Develop a Python program to generate the Fibonacci series using recursive and user-defined functions.
# Program to generate Fibonacci series using recursion


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Taking input from the user
terms = int(input("Enter the number of terms: "))

print("Fibonacci Series:")

if terms <= 0:
    print("Please enter a positive number.")
else:
    for i in range(terms):
        print(fibonacci(i), end=" ")
