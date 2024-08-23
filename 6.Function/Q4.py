# 4) Write a Program to Convert Decimal to Binary number manually by creating user-defined functions.

def decimal_to_binary(decimal_number):
    """Convert a decimal number to a binary number."""
    if decimal_number == 0:
        return "0"

    binary_str = ""
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_str = str(remainder) + binary_str
        decimal_number = decimal_number // 2

    return binary_str

def main():
    """Main function to get user input and convert decimal to binary."""
    decimal_number = int(input("Enter a decimal number: "))
    
    # Ensure the input is a non-negative integer
    if decimal_number < 0:
        print("Please enter a non-negative integer.")
        return
    
    binary_str = decimal_to_binary(decimal_number)
    print(f"The binary representation of decimal number {decimal_number} is {binary_str}")

if __name__ == "__main__":
    main()
