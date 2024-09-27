# 10) Write a Python program to find the largest word in a given String.
# Example:
# Sample Input: C++ is a general-purpose programming language.
# Sample Output: programming

def find_largest_word(string):
    """Function to find the largest word in a given string."""
    # Split the string into words
    words = string.split()
    # Initialize the largest word as the first word
    largest_word = words[0]
    
    # Iterate through all words to find the largest one
    for word in words:
        if len(word) > len(largest_word):
            largest_word = word
    
    return largest_word

def main():
    """Main function to get user input and find the largest word."""
    string = input("Enter a string: ")
    largest_word = find_largest_word(string)
    print(f"Largest word: {largest_word}")

if __name__ == "__main__":
    main()
