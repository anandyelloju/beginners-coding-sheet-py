# 3) Write a Program to Convert Binary Number to Decimal manually by creating user-defined functions.

def binary_to_decimal(binary_str):
    """Convert a binary number (as a string) to a decimal number."""
    decimal_number = 0
    power = 0

    # Reverse the binary string to process from least significant bit to most significant bit
    binary_str = binary_str[::-1]

    for digit in binary_str:
        if digit == '1':
            decimal_number += 2 ** power
        power += 1

    return decimal_number

def main():
    """Main function to get user input and convert binary to decimal."""
    binary_str = input("Enter a binary number: ")

    # Check if the input is a valid binary number
    if not all(char in '01' for char in binary_str):
        print("Invalid binary number")
        return

    decimal_number = binary_to_decimal(binary_str)
    print(f"The decimal representation of binary number {binary_str} is {decimal_number}")

if __name__ == "__main__":
    main()
