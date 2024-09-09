# 5) Write a Program that adds two matrices using Multidimensional Arrays where the number of rows r and columns c is entered by user (Value of r and c < 100)

def get_matrix(rows, cols):
    """Function to get a matrix from the user."""
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = float(input(f"Enter element [{i+1}][{j+1}]: "))
            row.append(value)
        matrix.append(row)
    return matrix

def add_matrices(matrix1, matrix2):
    """Function to add two matrices."""
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def display_matrix(matrix):
    """Function to display a matrix."""
    for row in matrix:
        print(' '.join(map(str, row)))

def main():
    """Main function to get user input and add two matrices."""
    try:
        r = int(input("Enter the number of rows (less than 100): "))
        c = int(input("Enter the number of columns (less than 100): "))
        
        if r >= 100 or c >= 100 or r <= 0 or c <= 0:
            print("Rows and columns must be between 1 and 99.")
            return
        
        print("Enter elements for the first matrix:")
        matrix1 = get_matrix(r, c)
        
        print("Enter elements for the second matrix:")
        matrix2 = get_matrix(r, c)
        
        result = add_matrices(matrix1, matrix2)
        
        print("The resulting matrix after addition is:")
        display_matrix(result)
    
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
