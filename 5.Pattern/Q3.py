# Print the below Pattern using loops in python
# 3) Half Pyramid Star Pattern
#    *
#    * *
#    * * *
#    * * * *
#    * * * * *

# Function to print a half pyramid star pattern
def print_half_pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print('*', end=' ')
        print()

# Define the number of rows
rows = 5

# Print the half pyramid star pattern
print_half_pyramid(rows)
