# 7) Write a Program that takes a matrix of order r*c from the user and computes the transpose of the matrix.

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

def transpose_matrix(matrix):
    """Function to compute the transpose of a matrix."""
    rows = len(matrix)
    cols = len(matrix[0])
    transpose = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = matrix[i][j]
    
    return transpose

def display_matrix(matrix):
    """Function to display a matrix."""
    for row in matrix:
        print(' '.join(map(str, row)))

def main():
    """Main function to get user input and compute the transpose of the matrix."""
    try:
        r = int(input("Enter the number of rows: "))
        c = int(input("Enter the number of columns: "))
        
        print("Enter elements for the matrix:")
        matrix = get_matrix(r, c)
        
        transpose = transpose_matrix(matrix)
        
        print("The transpose of the matrix is:")
        display_matrix(transpose)
    
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
