#   5) Write a Program to Check whether a year entered by user is Leap Year or not

year = int(input("Enter a year: ")) 
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): 
    print("{year) is a leap year. ") 
else: 
    print(f" (year) is not a leap year.")