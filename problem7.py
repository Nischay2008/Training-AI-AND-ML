# Write a program that takes the user weight and caluclate their BMI, categorize their BMI as underweight--> Below 50
# Normal weight --> 50-80 and Overweight --> Above 80

weight = int(input("Enter your weight "))

if weight <= 50:
    print("Underweight")
elif weight >= 80:
    print("Overweight.")
else:
    print("Normal Weight")