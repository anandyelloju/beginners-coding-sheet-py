# Print the below Pattern using loops in python
# 2) Hollow Rectangular star
# * * * * *
# *       *
# * * * * *


# Function to print a hollow rectangular star pattern
def print_hollow_rectangle(rows, columns):
    for i in range(rows):
        for j in range(columns):
            # Print star for the first and last row, or first and last column of middle rows
            if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

# Define the number of rows and columns
rows = 3
columns = 5

# Print the hollow rectangular star pattern
print_hollow_rectangle(rows, columns)
