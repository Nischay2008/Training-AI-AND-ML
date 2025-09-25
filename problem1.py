# Write a add, subract, multiply and division fucntion



def main():
    x = float(input("Enter number X: "))
    y = float(input("Enter number Y: "))

    operators = ["+", "-", "*", "/"]

    operation = input("Enter an operator (+, -, *, /): ")

    if operation not in operators:
        raise ValueError("Invalid Input. Retry.")
    elif operation == "+":
        add(x, y)
    elif operation == "-":
        subtract(x, y)
    elif operation == "*":
        multiply(x, y)
    elif operation == "/":
        divide(x, y)

def add(a, b):
    print(a + b)

def subtract(a, b):
    print(a - b)

def multiply(a, b):
    print(a * b)

def divide(a, b):
    if b == 0:
        print("Division by zero is not allowed.")
    else:
        print(a / b)

main()