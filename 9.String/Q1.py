# 1) Write a Program to Find the Frequency of given Character by user in a String

def find_char_frequency(string, char):
    """Function to find the frequency of a given character in a string."""
    frequency = string.count(char)
    return frequency

def main():
    """Main function to get user input and find the frequency of a given character."""
    string = input("Enter a string: ")
    char = input("Enter a character to find its frequency: ")
    
    if len(char) != 1:
        print("Please enter a single character.")
        return
    
    frequency = find_char_frequency(string, char)
    print(f"The frequency of '{char}' in the string is: {frequency}")

if __name__ == "__main__":
    main()
