# 1) Write a Program to Find Sum of N Natural Numbers (entered by users) using Recursion

def sum_of_natural_numbers(n):
    """Recursive function to find the sum of the first n natural numbers."""
    if n <= 0:
        return 0
    else:
        return n + sum_of_natural_numbers(n - 1)

def main():
    """Main function to get user input and calculate the sum of natural numbers."""
    n = int(input("Enter a positive integer: "))
    
    if n < 0:
        print("Please enter a positive integer.")
        return
    
    result = sum_of_natural_numbers(n)
    print(f"The sum of the first {n} natural numbers is: {result}")

if __name__ == "__main__":
    main()
