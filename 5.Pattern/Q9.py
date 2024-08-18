# Print the below Pattern using loops in python
# 9) Pascal Triangle
#  1
#  1 1
#  1 2 1
#  1 3 3 1
#  1 4 6 4 1

# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Function to calculate binomial coefficient
def binomial_coeff(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

# Function to print Pascal's Triangle
def print_pascals_triangle(rows):
    for i in range(rows):
        # Print leading spaces for formatting
        for j in range(rows - i - 1):
            print(' ', end=' ')
        # Print binomial coefficients
        for k in range(i + 1):
            print(binomial_coeff(i, k), end=' ')
        # Move to the next line after printing each row
        print()

# Define the number of rows
rows = 5

# Print Pascal's Triangle
print_pascals_triangle(rows)
