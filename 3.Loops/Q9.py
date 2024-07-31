# 9) Write a Program to display sum of all digits of a given Number N by user

num = input("Enter Number: ")
sum = 0

# Using String Extraction method
for i in num:
    sum = sum + int(i)

print(sum)

# Using Brute Force
num = int(num)
while num!=0:
	digit = int(num%10)
	sum += digit
	num = num/10

print(sum)

# Using Recursion I
def findSum(num, sum):
    if num == 0:
        return sum

    digit = int(num % 10)
    sum += digit
    return findSum(num / 10, sum)

print(findSum(int(num), sum))

# Using Recursion II
def findSum(num):
    if num == 0:
        return 0
    return int(num % 10) + findSum(num / 10)

print(findSum(int(num)))

# Using ASCII Table
for i in range(len(num)):
    # ord methods helps with ASCII
    sum += ord(num[i]) - 48

print(sum)

# Using map(), sum() and strip methods
def getSum(n):
    
    # fetch each individual char using strip method
    # find comparable int and store it in map
    # covert it into list
    list_of_number = list(map(int, n.strip()))
    
    print(list_of_number)
    
    # sum function returns the sum of all items in list
    return sum(list_of_number)
   
print(getSum(num))

# One Line recursive function
def sumDigits(n):
    return 0 if n == 0 else int(n % 10) + sumDigits(int(n / 10)) 
   
print(sumDigits(int(num)))

# The cool method
n = [int(d) for d in input("Enter the number : ")]
print("the sum of digits is : ", sum(n))

