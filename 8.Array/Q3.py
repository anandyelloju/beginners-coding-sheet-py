# 3) Write a Program that calculates the standard deviation of 10 data using arrays

import math

def get_numbers(n):
    """Function to get n numbers from the user and store them in a list."""
    numbers = []
    for i in range(n):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    return numbers

def calculate_mean(numbers):
    """Function to calculate the mean of a list of numbers."""
    return sum(numbers) / len(numbers)

def calculate_variance(numbers, mean):
    """Function to calculate the variance of a list of numbers."""
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance

def calculate_standard_deviation(variance):
    """Function to calculate the standard deviation from variance."""
    return math.sqrt(variance)

def main():
    """Main function to get user input and calculate the standard deviation."""
    n = 10
    print(f"Enter {n} numbers:")
    numbers = get_numbers(n)
    mean = calculate_mean(numbers)
    variance = calculate_variance(numbers, mean)
    standard_deviation = calculate_standard_deviation(variance)
    print(f"The standard deviation of the entered numbers is: {standard_deviation}")

if __name__ == "__main__":
    main()
