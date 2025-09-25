import time

print("Welcome to vote eligiblity testing app.")
login = False
while login == False:
    user = input("Enter your name: ")

    user_names = ["Nischay" , "Sidhaard"]

    if user not in user_names:
        raise ValueError("Invalid Login user.")

    password = input("Enter your password.")
    print(f"Your are password is {password}")


    con_pass = "MRCET@123"

    if password != con_pass:
        print("Invalid.")
    else:
        login = True
    

    
age = int(input(f"Enter your age {user} : "))

print("Thinking")
time.sleep(1)

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

print(f"{user} Thanks for using our app. Here we end the process if you wanna use again please reopen the app.")