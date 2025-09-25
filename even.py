def main():
    number = int(input("Enter a value: "))
    for x in number:
        if x % 2 == 0:
            print(f"{x} is a even number.\n")
            print(f"This loop breaks here because {x} is a first even number in the list.\n")
            print("Disclaimer: This is for educational purpose only.")
            break
        print(f"{x} is an odd number\n")
    else:
        print("There are no even numbers\n")
        print("Disclaimer: This is for educational purpose only.")
main()


