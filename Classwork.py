Student = input("Enter your name: ").capitalize()

student_names = ["Nischay" , "Siddhard" , "More can be added.."]

if Student not in student_names:
    raise ValueError("Invalid User.")

print(f"Hello {Student}, welcome to MRCET.")
print("Let's check if you are allowed to enter the college.")
print("Please show your ID card.")
id_card = "Scanned"

if id_card == "Scanned":
    print(f"Welcome {Student}. You are allowed to enter the college.")
else:
    print(f"Sorry {Student}. You are not allowed to enter the college.")

print("Let's check for your grade.")

marks = 80

while marks != 0:

    marks = int(input("Enter your marks: "))

    if marks > 95:
        print(f"Congratulations {Student}! You have secured A+ grade.")
    elif marks > 85:
        print(f"Congratulations {Student}! You have secured A grade.")
    elif marks > 75:
        print(f"Congratulations {Student}! You have secured B+ grade.")
    elif marks > 65:
        print(f"Congratulations {Student}! You have secured B grade.")
    elif marks > 55:
        print(f"Congratulations {Student}! You have secured C+ grade.")
    elif marks > 45:
        print(f"Congratulations {Student}! You have secured C grade.")
    elif marks > 35:
        print(f"Congratulations {Student}! You have secured D grade.")
    else:
        print(f"Sorry {Student}. You have secured F grade. Better luck next time.")
