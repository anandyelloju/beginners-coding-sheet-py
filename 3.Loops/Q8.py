#   8) Write a Program to Reverse a given Number N by user 

# using String slicing
num = input("Enter a number for reverse: ")
print(num[::-1])

# using While Loop
number = int(input("Enter the integer number: "))  
  
revs_number = 0  
  
while (number > 0):  
    remainder = number % 10  
    revs_number = (revs_number * 10) + remainder  
    number = number // 10  
  
print("The reverse number is :",revs_number) 

# using Recursion
revnum = 0
base_pos = 1;
 
def reverse(num):
    global revnum
    global base_pos
    if(num > 0):
        reverse((int)(num / 10))
        revnum += (num % 10) * base_pos
        base_pos *= 10
    return revnum
 
num = 12345
print(reverse(num))