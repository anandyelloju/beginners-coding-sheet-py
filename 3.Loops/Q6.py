#   6) Write a Program to Find GCD or HCF of two numbers entered by user 

# Python code to demonstrate the working of gcd()
# importing "math" for mathematical operations
import math

n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
print(math.gcd(n1, n2))


# Function to find GCD or HCF the Using Euclidian algorithm
def compute_gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
gcd = compute_gcd(n1, n2)
print("The GCD or HCF is", gcd)