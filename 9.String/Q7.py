# 7) Write a Python program to check if a given string is a Palindrome or not.

def is_palindrome(string):
    """Function to check if a string is a palindrome."""
    # Normalize the string by removing spaces and converting to lowercase
    normalized_string = ''.join(char.lower() for char in string if char.isalnum())
    # Check if the normalized string is equal to its reverse
    return normalized_string == normalized_string[::-1]

def main():
    """Main function to get user input and check if it is a palindrome."""
    string = input("Enter a string: ")
    if is_palindrome(string):
        print(f"'{string}' is a palindrome.")
    else:
        print(f"'{string}' is not a palindrome.")

if __name__ == "__main__":
    main()
