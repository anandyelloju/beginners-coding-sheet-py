# 4) Write a Program that calculates the power of a number using recursion where base and exponent is entered by the user.

def power(base, exponent):
    """Recursive function to calculate the power of a number."""
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

def main():
    """Main function to get user input and calculate the power."""
    base = float(input("Enter the base number: "))
    exponent = int(input("Enter the exponent: "))
    
    if exponent < 0:
        print("Please enter a non-negative exponent.")
        return
    
    result = power(base, exponent)
    print(f"{base} raised to the power of {exponent} is: {result}")

if __name__ == "__main__":
    main()
