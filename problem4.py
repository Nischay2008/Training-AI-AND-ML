# Write a programme to caluclate a square and cude of a number without using (*) operator, use multiplication instead.

def main():
    x = int(input("Enter the value X: "))

    operators = ["2", "3"]
    operation = input("Enter an operator for square 2 and for cube 3 (2,3): ")

    if operation not in operators:
        print("Invalid Input")
    elif operation == "2":
        square(x)
    elif operation == "3":
        cube(x)
    
def square(a):
    print(a * a)
def cube(b):
    print(b * b * b)

main()