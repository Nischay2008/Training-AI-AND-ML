import time

hot = input("Is your laptop hot? Type your answer in (Y/N)").lower()

if hot == "y":
    print("Please connect the charger. To turn on the cooling system.")
    connect = input("Have you connected the charger? Type (Y/N)").lower()
else:
    print("Thats great that your laptop is cool.")

if hot == "y" and connect == "y":
    print("The cooling system has started. Please wait until we cooldown your laptop.")