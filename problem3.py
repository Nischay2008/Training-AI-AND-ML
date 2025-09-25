# Write a program to check weather the given number is divisible by 3 and 5 using logical operators(And or)

x = int(input("Enter value X: "))

m5 = (x % 5 == 0)
m3 = (x % 3 == 0)

if m3 and m5:
    print(f"{x} is divisible by both 3 and 5.")
else:
    print(f"{x} is not divisible by both 3 and 5.")