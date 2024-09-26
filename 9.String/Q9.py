# 9) Write a Python program to capitalize the first letter of each word of a given string. Words must be separated by only one space
# Example:
# Sample Input: cpp string exercises
# Sample Output: Cpp String Exercises

def capitalize_words(string):
    """Function to capitalize the first letter of each word in a given string."""
    # Split the string into words, capitalize each word, and join them back with a space
    capitalized_string = ' '.join(word.capitalize() for word in string.split(' '))
    return capitalized_string

def main():
    """Main function to get user input and capitalize each word."""
    string = input("Enter a string: ")
    capitalized_string = capitalize_words(string)
    print(f"Output: {capitalized_string}")

if __name__ == "__main__":
    main()
