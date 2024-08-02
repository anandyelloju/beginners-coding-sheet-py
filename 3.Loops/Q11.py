# 11) Write a Program to Calculate Power of a Number without using inbuilt pow() function by taking two inputs from users as Base and exponent respectively

base, exponent = map(int, input("Enter base and expo: ").split())

# Using Arithmetic Operator
power = base ** exponent

# Using for loop
power = 1
for _ in range(exponent):
    power *= base

# Using While loop
power, expo = 1, exponent
while expo != 0:
    power *= base
    expo -= 1

print(f"{base} raised to the power of {exponent} is {power}")