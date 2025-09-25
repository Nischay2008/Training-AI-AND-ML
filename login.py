while True:
    username = input("Please enter your username: ").capitalize()
    user_data = ["Nischay" , "Mrcet"]
    if username not in user_data[0]:
        raise ValueError("Invalid User. Try again.")    
    password = input(f"{username} Please enter your password: ").capitalize()
    pass_data = ["Nischay@123"]
    if password not in pass_data[0]: 
       raise ValueError("Invalid Password")
    print(f"{username} You have successfully logined.")
    break