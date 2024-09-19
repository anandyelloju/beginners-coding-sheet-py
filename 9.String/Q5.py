# 5) Write a Program to Concatenate (join) Two Strings entered by user

def concatenate_strings(string1, string2):
    """Function to concatenate two strings."""
    concatenated_string = string1 + string2
    return concatenated_string

def main():
    """Main function to get user input and concatenate two strings."""
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    result = concatenate_strings(string1, string2)
    print(f"The concatenated string is: {result}")

if __name__ == "__main__":
    main()
