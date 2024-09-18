# 4) Write a Program to Find the Length of a String entered by user

def find_length(string):
    """Function to find the length of a string."""
    length = len(string)
    return length

def main():
    """Main function to get user input and find the length of the string."""
    string = input("Enter a string: ")
    length = find_length(string)
    print(f"The length of the string is: {length}")

if __name__ == "__main__":
    main()
