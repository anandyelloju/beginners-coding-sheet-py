# 3) Write a Program to Remove all Characters in a String Except Alphabets.
# Example:
# Enter a string: p2'r"o@gram84iz./
# Output String: programiz

def remove_non_alphabets(string):
    """Function to remove all non-alphabet characters from a string."""
    result = ''.join([char for char in string if char.isalpha()])
    return result

def main():
    """Main function to get user input and remove non-alphabet characters."""
    string = input("Enter a string: ")
    cleaned_string = remove_non_alphabets(string)
    print(f"Output String: {cleaned_string}")

if __name__ == "__main__":
    main()
