# 2) Write a Program to Calculate Factorial of a Number Using Recursion

def factorial(n):
    """Recursive function to calculate the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    """Main function to get user input and calculate the factorial."""
    n = int(input("Enter a non-negative integer: "))
    
    if n < 0:
        print("Please enter a non-negative integer.")
        return
    
    result = factorial(n)
    print(f"The factorial of {n} is: {result}")

if __name__ == "__main__":
    main()
