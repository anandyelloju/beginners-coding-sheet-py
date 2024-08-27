# 3) Write a Program to Find G.C.D of two numbers entered by user Using Recursion

def gcd(a, b):
    """Recursive function to find the GCD of two numbers."""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def main():
    """Main function to get user input and calculate the GCD."""
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    if num1 < 0 or num2 < 0:
        print("Please enter non-negative integers.")
        return
    
    result = gcd(num1, num2)
    print(f"The G.C.D of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()
