    # 6) Write a Program takes two matrices of order r1*c1 and r2*c2 respectively. Then, the program multiplies these two matrices (if possible) and displays it on the screen.

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

def multiply_matrices(matrix1, matrix2):
    """Function to multiply two matrices."""
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

def display_matrix(matrix):
    """Function to display a matrix."""
    for row in matrix:
        print(' '.join(map(str, row)))

def main():
    """Main function to get user input and multiply two matrices."""
    try:
        r1 = int(input("Enter the number of rows for the first matrix: "))
        c1 = int(input("Enter the number of columns for the first matrix: "))
        
        r2 = int(input("Enter the number of rows for the second matrix: "))
        c2 = int(input("Enter the number of columns for the second matrix: "))
        
        if c1 != r2:
            print("Matrix multiplication is not possible. The number of columns in the first matrix must be equal to the number of rows in the second matrix.")
            return
        
        print("Enter elements for the first matrix:")
        matrix1 = get_matrix(r1, c1)
        
        print("Enter elements for the second matrix:")
        matrix2 = get_matrix(r2, c2)
        
        result = multiply_matrices(matrix1, matrix2)
        
        print("The resulting matrix after multiplication is:")
        display_matrix(result)
    
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
