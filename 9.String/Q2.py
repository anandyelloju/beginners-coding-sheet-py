# 2) Write a Program to Find the Number of Vowels, Consonants, Digits and White Spaces in a String

def count_characters(string):
    """Function to count vowels, consonants, digits, and white spaces in a string."""
    vowels = "aeiouAEIOU"
    num_vowels = num_consonants = num_digits = num_spaces = 0
    
    for char in string:
        if char.isdigit():
            num_digits += 1
        elif char.isspace():
            num_spaces += 1
        elif char.isalpha():
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1
    
    return num_vowels, num_consonants, num_digits, num_spaces

def main():
    """Main function to get user input and count characters."""
    string = input("Enter a string: ")
    
    num_vowels, num_consonants, num_digits, num_spaces = count_characters(string)
    
    print(f"Number of vowels: {num_vowels}")
    print(f"Number of consonants: {num_consonants}")
    print(f"Number of digits: {num_digits}")
    print(f"Number of white spaces: {num_spaces}")

if __name__ == "__main__":
    main()
