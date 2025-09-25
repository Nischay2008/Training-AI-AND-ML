# Write a program to check whether a given number is muptiple of 3 and 5 or not(Conditional statement)

x = int(input("Enter the valye X: "))

if x % 3 == 0 and not x % 5 == 0:
    print("Divisible by 3")
elif x % 5 == 0 and not x % 3 == 0:
    print("Divisble by 5")
elif x % 5 == 0 and x % 3 == 0:
    print("Divisible by both")