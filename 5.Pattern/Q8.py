# Print the below Pattern using loops in python
# 8) Half pyramid using numbers
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# Function to print a half pyramid using numbers
def print_half_pyramid_numbers(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

# Define the number of rows
rows = 5

# Print the half pyramid using numbers
print_half_pyramid_numbers(rows)
