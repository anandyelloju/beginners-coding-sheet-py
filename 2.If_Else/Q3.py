# 3) Write a Program to Find Largest Number Among Three Numbers entered by users
print("Enter 3 numbers")

n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
n3 = int(input("Number 3: "))

# method 1 
print("The Largest number is ", max(n1,n2,n3))

# method 2
if n1>n2 and n1>n3:
    print("The Largest number is ", n1)
elif n2>n1 and n2>n3:
    print("The Largest number is ", n2)
else: 
    print("The Largest number is ", n3)