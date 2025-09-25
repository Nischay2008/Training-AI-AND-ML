username = input("Enter your username: ").capitalize()
username_c = ['Nischay' , 'Mrcet']
if username not in username_c:
    print(f"I guess you are a new user {username}. We will take you in and soon be added in our data-base.")
while True:
    x = input(f"Enter 'exit' {username} to stop the VIRUS: ").lower()
    if x == "exit":
        print(f"You have exited the VIRUS {username}.")
        break
    print(f"Just type exit kid. There is VIRUS to continue. Kid = {username}")
        