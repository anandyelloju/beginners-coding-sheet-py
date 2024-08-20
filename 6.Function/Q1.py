# 1) Write a Program to Display Prime Numbers Between Two Intervals (entered by the user) Using Functions

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    """Find all prime numbers in a given range."""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def main():
    """Main function to get user input and display prime numbers."""
    # Get the intervals from the user
    start = int(input("Enter the starting number of the interval: "))
    end = int(input("Enter the ending number of the interval: "))

    # Find and display prime numbers in the range
    primes = find_primes_in_range(start, end)
    print(f"Prime numbers between {start} and {end} are: {primes}")

if __name__ == "__main__":
    main()
