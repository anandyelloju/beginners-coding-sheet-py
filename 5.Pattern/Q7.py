# Print the below Pattern using loops in python
# 7)Hollow Full Pyramid Star
#         *
#       * *
#     *   *
#   *     *
# *********

# Function to print a hollow full pyramid star pattern
def print_hollow_full_pyramid(rows):
    for i in range(rows):
        # Print leading spaces
        for j in range(rows - i - 1):
            print(' ', end=' ')
        # Print stars and spaces
        for k in range(2 * i + 1):
            # Print star for the first and last star in each row, and the last row
            if k == 0 or k == 2 * i or i == rows - 1:
                print('*', end='')
            else:
                print(' ', end='')
        # Move to the next line after printing each row
        print()

# Define the number of rows
rows = 5

# Print the hollow full pyramid star pattern
print_hollow_full_pyramid(rows)
