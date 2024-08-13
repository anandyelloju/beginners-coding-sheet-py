# Print the below Pattern using loops in python
# 4) Inverted Half pyramid
#    * * * * * *
#    * * * * *
#    * * * *
#    * * *
#    * *
#    *

# Function to print an inverted half pyramid star pattern
def print_inverted_half_pyramid(rows):
    for i in range(rows, 0, -1):
        for j in range(i):
            print('*', end=' ')
        print()

# Define the number of rows
rows = 6

# Print the inverted half pyramid star pattern
print_inverted_half_pyramid(rows)
