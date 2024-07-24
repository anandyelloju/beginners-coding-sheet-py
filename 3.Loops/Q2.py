#   2) Write a Program to Find Factorial of a given number N (N is entered by user) 

n = int(input("Eneter Nth number: "))
fact = 1
for i in range(1,n+1):
    fact *= i
print("Sum of", n, "natural numbers is", fact)