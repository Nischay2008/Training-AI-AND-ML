# Write a problem that takes an input of an 2 numbers and find reminder(Modulas) and quotient of thier division.

def main():

    x = int(input("Enter number X: "))
    y= int(input("Enter number Y: "))

    operator = ("%" , "/")

    operation = input("Enter a operator (%,/)")

    if operation not in operator:
        print("Invalid Value")
    elif operation == "%":
        reminder(x, y)
    elif operation == "/":
        quotient(x, y)

def reminder(a, b):
    print(a % b)

def quotient(a, b):
    print(a / b)

main()