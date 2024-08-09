# 1) Write a Program to Make a Simple Calculator to Add, Subtract, Multiply or Divide Using Switch case The program should takes an arithmetic operator (+, -, * , /) and two operands from a user and performs the operation on those two operands depending upon the operator entered by the user.

# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Function to perform calculation based on the operator
def calculate(operator, x, y):
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    if operator in operations:
        return operations[operator](x, y)
    else:
        return "Invalid operator!"

# Taking input from the user
operator = input("Enter an operator (+, -, *, /): ")
x = float(input("Enter the first operand: "))
y = float(input("Enter the second operand: "))

# Performing the calculation and displaying the result
result = calculate(operator, x, y)
print(f"The result of {x} {operator} {y} is: {result}")