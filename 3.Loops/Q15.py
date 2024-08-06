# 15) Write a Program to check whether a number entered by the user is an Armstrong number or not.

# Function to check if a number is an Armstrong number
def is_armstrong(number):
    digits = [int(digit) for digit in str(number)]
    num_digits = len(digits)
    sum_of_powers = 0
    for digit in digits:
        sum_of_powers += digit ** num_digits
    return sum_of_powers == number

# Taking input from the user
number = int(input("Enter a number: "))

# Checking if the number is an Armstrong number
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
