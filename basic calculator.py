import math
print("welcome to the basic calculator app!")
def add(x,y):
    print(f"{x} + {y} = {x+y}")
def substract(x,y):
    print(f"{x} - {y} = {x-y}")
def multiply(x,y):
    print(f"{x} * {y} = {x*y}")
def divide(x,y):
    if y == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"{x} / {y} = {x/y}")
def power(x,y):
    print(f"{x} ^ {y} = {math.pow(x,y)}")
def square_root(x):
    if x < 0:
        print("Error: Cannot calculate square root of a negative number.")
    else:
        print(f"√{x} = {math.sqrt(x)}")
print("enter two numbers:")
num1=float(input("first number: "))
num2=float(input("second number: "))
print("enter the operation you want to perform: from the following options:add,substract,multiply,divide,power,square_root")
operation=input("operation: ").strip().lower()
if operation == "add":
    add(num1, num2)
elif operation == "substract":
    substract(num1, num2)
elif operation == "multiply":
    multiply(num1, num2)
elif operation == "divide":
    divide(num1, num2)
elif operation== "power":
    power(num1,num2)
elif operation=="square_root":
    square_root(num1)
else:
    print("Invalid operation. Please choose from: add, substract, multiply, divide, power, square_root.")