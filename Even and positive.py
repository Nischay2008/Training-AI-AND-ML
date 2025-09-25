
while True:

    x = int(input("Enter a number: "))

    if x % 2 == 0 and x > 0:
        print(f"The number {x} is even and positive.")
    elif x % 2 == 0 and x < 0:
        print(f"The number {x} is even but not positive.")
    elif x % 2 != 0 and x > 0:
        print(f"The number {x} is not a even number and it is a positive number.")
    else:
        print(f"The number {x} is not even or positive.")