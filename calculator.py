languages = ["English" , "Telugu" , "Hindi"]  # Add supported languages here


def main():

    name = input("Enter your username. ").lower()
    print(f"Hello {name} You are most welcomed.")
    while True:
        password = input("Enter your password.")
        print(f"Your password is {password}. Please confirm it again.")
        confirm_password = input("Enter your password again to confirm.")

        if password == confirm_password:
            print(f"Your password is {confirm_password}. It is verified. The length of the password is ", len(
                confirm_password))
            break
        else:
            print("Password do not match. Try again. \n")

    lang = input("Choose your language: ").capitalize()
    if lang not in languages:
        raise ValueError("Language not supported.")
    else:
        print(f"You have chosen {lang} as your language.\n")

    if lang == "English":
        print(
            "Welcome to calculator app made by MRCET Student with guidance of Mr.Siddharth.")

    x = float(input("Enter the value of X =  "))  # For entering the value of X
    y = float(input("Enter the value of Y =  "))  # For entering the value of Y

    # Symbols of Addition,Subtraction,Multiplication and Division.
    Calc = ["+", "-", "x", "/"]

    Calculator_Symbols = input("Enter the operators(+ , - , x , /): ")

    if Calculator_Symbols not in Calc:
        raise ValueError
    elif Calculator_Symbols == "+":
        add(x, y)
    elif Calculator_Symbols == "-":
        subtract(x, y)
    elif Calculator_Symbols == "x":
        multiply(x, y)
    elif Calculator_Symbols == "/":
        divide(x, y)


def add(a, b):
    print(a + b)


def subtract(a, b):
    print(a - b)


def multiply(a, b):
    print(a * b)


def divide(a, b):
    if b == 0:
        print("Invalid")
    else:
        print(a/b)


if __name__ == "__main__":
    while True:

        main()

