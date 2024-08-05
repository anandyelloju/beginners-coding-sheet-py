# 14) Write a Program to Display Prime Numbers Between Two Intervals (entered by user) Example: Enter two numbers: 0 20 Prime numbers between 0 and 20 are: 2 3 5 7 11 13 17 19

# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Function to display prime numbers between two intervals
def display_primes_between_intervals(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Taking input from the user
start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

# Getting prime numbers in the interval
prime_numbers = display_primes_between_intervals(start, end)

# Displaying the prime numbers
print(f"Prime numbers between {start} and {end} are: {', '.join(map(str, prime_numbers))}")
