# 6) Inverted Full pyramid
# * * * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *

# Function to print an inverted full pyramid star pattern
def print_inverted_full_pyramid(rows):
    for i in range(rows, 0, -1):
        # Print leading spaces
        for j in range(rows - i):
            print(' ', end=' ')
        # Print stars
        for k in range(i):
            print('*', end=' ')
        # Move to the next line after printing each row
        print()

# Define the number of rows
rows = 6

# Print the inverted full pyramid star pattern
print_inverted_full_pyramid(rows)
