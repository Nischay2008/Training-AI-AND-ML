import random

ass = 10

marks = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13 ,14 ,15 ,16 ,17 ,18 ,19 ,20 ,21 ,22 ,23 ,24 ,25 ,26 ,27 ,28 ,29 ,30]

while marks:

    print("Welcome to the Marks Predictor! of your internal exams.")
    print("Disclaimer: This is just a prediction and may not be accurate. This is for entertainment purposes only. Do not take it seriously.")
    name = input("Enter your name according to SSC Board: ").capitalize()

    x = random.choice(marks) + ass
    y = random.choice(marks)

    assign = input("Did you complete all your assignments? (yes/no): ").lower()

    if assign == "yes":
        print(f"Congratulations {name}! You have completed all your assignments.")
        print(f"Your predicted marks are: {x}/40")
    else:
        print(f"Sorry {name}. You have not completed all your assignments.")
        print(f"Your predicted marks are: {y}/40")

        