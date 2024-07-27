#   5) Write a Program to Display Fibonacci Series upto certain number n (n is entered by user) 
#   Example: n=100 Output: Fibonacci Series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 

# Program to display the Fibonacci sequence up to n-th term
nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
# generate fibonacci sequence
else:
    print("Fibonacci sequence:")
    fib = []
    while count < nterms:
       # print(n1)
       if n1 > nterms:
           break
       nth = n1 + n2
       fib.append(n1)
       # update values
       n1 = n2
       n2 = nth
       count += 1

    print(*fib,sep=", ")