# 6) Write a python program to change every letter in a given string with the letter following it in the alphabet (ie. a becomes b, p becomes q, z becomes a).
# Example:
# Sample Input: Abcdef3
# Sample Output: Bcdefg3

def shift_letter(letter):
    """Function to shift a letter to the next letter in the alphabet."""
    if 'a' <= letter <= 'z':
        return 'a' if letter == 'z' else chr(ord(letter) + 1)
    elif 'A' <= letter <= 'Z':
        return 'A' if letter == 'Z' else chr(ord(letter) + 1)
    else:
        return letter

def shift_string(input_string):
    """Function to shift every letter in the string to the next letter in the alphabet."""
    return ''.join(shift_letter(char) for char in input_string)

def main():
    """Main function to get user input and shift every letter in the string."""
    input_string = input("Enter a string: ")
    output_string = shift_string(input_string)
    print(f"Sample Output: {output_string}")

if __name__ == "__main__":
    main()
