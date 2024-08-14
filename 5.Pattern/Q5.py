# Print the below Pattern using loops in python
# 5) Full Pyramid Star Pattern
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# * * * * * *

# Function to print a full pyramid star pattern
def print_full_pyramid(rows):
    for i in range(rows):
        # Print leading spaces
        for j in range(rows - i - 1):
            print(' ', end=' ')
        # Print stars
        for k in range(i + 1):
            print('*', end=' ')
        # Move to the next line after printing each row
        print()

# Define the number of rows
rows = 6

# Print the full pyramid star pattern
print_full_pyramid(rows)
