#   1) Write a Program to Calculate Sum of first N Natural Numbers (here value of N is Entered by user) 

n = int(input("Eneter Nth number: "))
sum = 0
for i in range(n+1):
    sum += i
print("Sum of ", n, " natural numbers is ", sum)
