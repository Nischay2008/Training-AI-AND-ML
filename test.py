'''
1. Write a function mul_numbers(a , b) that returns the mul of a and b.
1. The functions should check if the number is even or odd and print:
3. The function should return the factorial of n.
4. Write a function largest_of_three(a,b,c)
5.Reverse_strings(s)
6. The function should return the number of vowels(a,e,i,o,u) in the string passed.'''

#1 
def main():

    print("1 Problem:-")

    Mx = int(input("Enter value of A: "))
    My = int(input("Enter value of B: "))

    operator = ["x"]
    op = input("Enter the multiplication operator: 'x'")
    if op not in operator:
        raise ValueError("Invalid Operator.")

    if op == "x":
        multiply(Mx , My)

def multiply(a , b):
    print("Answer is ", a * b)

main()

# 2 
print("2nd Problem:-")

eo = int(input("Enter value of X: "))

if eo % 2 == 0 and not eo % 3 == 0:
    print(f"{eo} is a even number.")
elif eo % 3 == 0 and not eo % 3 == 0:
    print(f"{eo} is a even number.")

#3 
print("3rd Problem:- ")

def main():
    num = int(input("Enter value of X: "))
    print(f"{num}! = {factorial(num)} ")

def factorial(a):
    if a == 0  or a == 1:
        return 1
    result = 1
    for i in range(a , a+1):
        result *= 1
    return result

main()

#4 
def main():
    print("4 Problem.")

    a = int(input("Enter value X: "))
    b = int(input("Enter value Y: "))
    c = int(input("Enter value Z: "))

    print(maximum(a , b , c))

def maximum(x , y , z):
    numbers = (x,  y , z)
    init = x
    for f in numbers:
        if f > init:
            init = f
    return init
main()

#5 
print("Problem 5")

# i1 = int(input("Enter value of x: "))
# i2 = int(input("Enter value of y: "))
# i3 = int(input("Enter value of z: "))

# c = (i1 , i2 , i3)

# print(c[::-1])
def main():
    i4 = input("Enter a Word: ")
    reverse(i4)

def reverse(text):
    return text[::-1]
main()
# 6

print("Problem 6")


