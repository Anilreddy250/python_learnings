def factorial(n):
    # Base case: 1! or 0! is always 1
    if n <= 1:
        return 1
    # Recursive step: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120