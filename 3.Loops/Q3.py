#   3) Write a Program to Generate Multiplication Table of a number (entered by the user) using a for loop. 

n = int(input("Eneter a number: "))
print("Multiplication Table of", n)
for i in range(1,11):
    print(n, "*", i, "=", n*i)