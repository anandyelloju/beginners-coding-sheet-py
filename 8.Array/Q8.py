# 8) Write a Program that takes three integers from the user and swaps them in cyclic order using pointers.
# Example:
# Enter value of a, b and c respectively:1 2 3
# Value after swapping numbers in cycle:
# a=3
# b=1
# c=2

def swap_cyclic(a, b, c):
    """Function to swap three integers in cyclic order."""
    return c, a, b

def main():
    """Main function to get user input and swap integers in cyclic order."""
    try:
        a = int(input("Enter the value of a: "))
        b = int(input("Enter the value of b: "))
        c = int(input("Enter the value of c: "))
        
        print(f"Original values:\na = {a}\nb = {b}\nc = {c}")
        
        a, b, c = swap_cyclic(a, b, c)
        
        print(f"Values after swapping in cyclic order:\na = {a}\nb = {b}\nc = {c}")
    
    except ValueError:
        print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()

