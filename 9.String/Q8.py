# 8) Write a Python program to count all the words in a given string. Words must be separated by only one space.
# Example:
# Sample Input: Siddharth Singh
# Sample Output: number of words -> 2

def count_words(string):
    """Function to count all the words in a given string."""
    # Split the string into words using space as the delimiter
    words = string.split(' ')
    # Count the number of words
    return len(words)

def main():
    """Main function to get user input and count the number of words."""
    string = input("Enter a string: ")
    word_count = count_words(string)
    print(f"Number of words -> {word_count}")

if __name__ == "__main__":
    main()
