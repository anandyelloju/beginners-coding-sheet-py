# 12) Write a Program to Check Whether a Number N entered by user is Palindrome or Not

# Using string reversal
num = input("Enter a number: ")
if num == num[::-1]:
    print("{num} is a Palindrome")
else:
    print("{num} is not a Palindrome")

# Using while loop
num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print(f"{temp} is a Palindrome")
else:
    print(f"{temp} is not a Palindrome")