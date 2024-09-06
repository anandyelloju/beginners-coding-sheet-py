# 2) Write a Program that takes n element from user and displays the largest element of an array

def get_numbers(n):
    """Function to get n numbers from the user and store them in a list."""
    numbers = []
    for i in range(n):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    return numbers

def find_largest(numbers):
    """Function to find the largest element in a list of numbers."""
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

def main():
    """Main function to get user input and find the largest element in an array."""
    try:
        n = int(input("Enter the number of elements: "))
        
        if n < 0:
            print("Number of elements cannot be negative.")
            return
        
        numbers = get_numbers(n)
        largest = find_largest(numbers)
        
        if largest is None:
            print("The list is empty. No largest element.")
        else:
            print(f"The largest element in the array is: {largest}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
