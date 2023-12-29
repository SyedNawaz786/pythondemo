def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Replace 'n' with the desired number
n = 4

# Calculate factorial using the factorial function
factorial_result = factorial(n)

print(f"The factorial of {n} is: {factorial_result}")
