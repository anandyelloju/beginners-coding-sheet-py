# 1) Write a Program that takes N elements (max. value of N is 100 and N is the float number specified by user) from user, stores data in an array and Calculates the average of those numbers.

def get_numbers(n):
    """Function to get N numbers from the user and store them in a list."""
    numbers = []
    for i in range(n):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    return numbers

def calculate_average(numbers):
    """Function to calculate the average of a list of numbers."""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def main():
    """Main function to get user input and calculate the average of N numbers."""
    try:
        n = int(float(input("Enter the number of elements (max 100): ")))
        
        if n < 0:
            print("Number of elements cannot be negative.")
            return

        if n > 100:
            print("Number of elements cannot exceed 100.")
            return
        
        numbers = get_numbers(n)
        average = calculate_average(numbers)
        print(f"The average of the entered numbers is: {average}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
