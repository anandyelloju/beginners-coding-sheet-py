#   7) Write a Program to Find LCM of two numbers entered by user

import math

def lcm(a, b):
    lcm = (a * b) // math.gcd(a, b)
    return lcm

n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
print(lcm(n1, n2))