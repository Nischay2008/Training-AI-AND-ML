#  Write a program to check whether a given number is divisible by 4 or 5(Conditional statement)

x = int(input("Enter value X: "))

if x % 4 == 0 and not x % 5 == 0:
    print("Divisible by 4")
elif x % 5 == 0 and not x % 4 == 0:
    print("Divisible by 5")
elif x % 4 == 0 and x % 5 == 0:
    print("Divisble by both.")
