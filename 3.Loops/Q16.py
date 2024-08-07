# 16) Write a Program to Display all Factors of a Number entered by User

import math

# Function to find all factors of a number
def find_factors(number):
    factors = set()
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.add(i)
            factors.add(number // i)
    return sorted(factors)

# Taking input from the user
number = int(input("Enter a number: "))

# Finding factors of the number
factors = find_factors(number)

# Displaying the factors
print(f"The factors of {number} are: {factors}")
