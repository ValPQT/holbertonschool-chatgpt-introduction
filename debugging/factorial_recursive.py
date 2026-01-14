#!/usr/bin/python3
import sys

def factorial(n):
    """
    factorial - computes the factorial of a number using recursion

    @n: integer whose factorial is to be calculated
    Return: factorial of n
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get the number from command-line arguments
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
