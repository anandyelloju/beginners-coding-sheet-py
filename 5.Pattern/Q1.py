# Print the below Pattern using loops
# 1) Solid Rectangular star
#    * * * * *
#    * * * * *
#    * * * * *

# Function to print a solid rectangular star pattern
def print_solid_rectangle(rows, columns):
    for i in range(rows):
        for j in range(columns):
            print('*', end=' ')
        print()

# Define the number of rows and columns
rows = 3
columns = 5

# Print the solid rectangular star pattern
print_solid_rectangle(rows, columns)
