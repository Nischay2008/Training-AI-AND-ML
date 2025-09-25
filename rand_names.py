import random

data = ["Nischay" , "Madhu" , "Nice"]

while True:
    rand = random.choices(data)
    print("I will guess your name, If my guess is correct type Yes, if it is not right type No.\n")
    print(f"Your name is {rand} right?")
    m = input("Yes (or) No: ").capitalize()
    if m == "Yes":
        print("I am always right, Bye")
        break
    elif m == "No":
        print("I will take an other guess.")
        continue