# 2) Write a Program to check if an integer(entered by the user) can be expressed as the sum of two prime numbers,if yes then print all possible combinations with the use of functions. Example
# Enter a positive integer: 34
# OUTPUT:
# 34 = 3 + 31
# 34 = 5 + 29
# 34 = 11 + 23
# 34 = 17 + 17

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_prime_pairs(n):
    """Find all pairs of prime numbers that sum up to n."""
    prime_pairs = []
    for i in range(2, n):
        if is_prime(i) and is_prime(n - i):
            prime_pairs.append((i, n - i))
    return prime_pairs

def main():
    """Main function to get user input and find prime pairs."""
    n = int(input("Enter a positive integer: "))
    
    prime_pairs = find_prime_pairs(n)
    if prime_pairs:
        print(f"{n} can be expressed as the sum of the following pairs of prime numbers:")
        for pair in prime_pairs:
            print(f"{n} = {pair[0]} + {pair[1]}")
    else:
        print(f"{n} cannot be expressed as the sum of two prime numbers.")

if __name__ == "__main__":
    main()
