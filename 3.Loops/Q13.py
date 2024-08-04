# 13) Write a Program to Check Whether a Number is Prime or Not

# Basic iterative approach to check if a number is prime
def is_prime_basic(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# Optimized approach to check if a number is prime
def is_prime_optimized(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Taking input from the user
number = int(input("Enter a number: "))

# Choosing the method
print("Choose the method to check prime:")
print("1. Basic Iterative")
print("2. Optimized Iterative")
method = int(input("Enter the method number (1/2): "))

# Checking if the number is prime based on the chosen method
if method == 1:
    result = is_prime_basic(number)
elif method == 2:
    result = is_prime_optimized(number)
else:
    print("Invalid method number!")
    result = None

# Displaying the result if a valid method was chosen
if result is not None:
    if result:
        print(f"The number {number} is prime.")
    else:
        print(f"The number {number} is not prime.")

