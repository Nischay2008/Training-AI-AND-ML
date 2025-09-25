import random

print("Welcome to rapido app.")


delay_x = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
delay = random.choices(delay_x)


bike = True
car = True
ac_car = True

surge = True

km_1 = 20


lang = ["english", "telugu", "hindi"]

Language = input(
    "Please choose the language. (English , Telugu , Hindi)").lower()
print("")
if Language not in lang:
    raise ValueError("Invalid Language please choose from the list provided.")

num = int(input("Please enter your phone number to login"))
print("")
password = input("Please enter your password to login")
print("")
confirm_password = input("Please confirm your password")
print("")
if password != confirm_password:
    raise ValueError("Password does not match. Try again.")

otp = 12345
otp_1 = int(input("Please enter the OTP(12345)"))
print("")

if otp_1 != otp:
    raise ValueError("Incorrect OTP. Try again.")

Ride = ["bike", "car", "ac_car"]

drop = input("Please enter your drop location")
print("")
km = int(input("Please enter the distance in KM's"))
print("")
vec = input(
    "Please enter the ride you choose from the list.(Bike , Car, AC_car)").lower()

if vec not in Ride:
    raise ValueError("Invalid Ride veh. Try again.")

if vec == "bike":
    print("You have chosen bike. Your ride is on the way.")
    print(
        f"Your ride will arrive in {delay} minutes and the fare is Rs {km_1*km*0.5}")
elif surge == True and vec == "bike":
    print("You have chosen bike. Your ride is on the way.")
    print(
        f"Your ride will arrive in {delay} minutes and the fare is Rs {km_1*km*0.5 + 10}")

if vec == "car":
    print("You have chosen car. Your ride is on the way.")
    print(f"Your ride will arrive in {delay} minutes and the fare is Rs {km_1*km*2}")
elif surge == True and vec == "car":
    print("You have chosen car. Your ride is on the way.")
    print(
        f"Your ride will arrive in {delay} minutes and the fare is Rs {km_1*km*2 + 30}")

if vec == "ac_car":
    print("You have chosen ac-car. Your ride is on the way.")
    print(f"Your ride will arrive in {delay} minutes and the fare is Rs {km_1*km*5}")
elif surge == True and  vec == "ac-car":
    print("You have chosen ac-car. Your ride is on the way.")
    print(
        f"Your ride will arrive in {delay} minutes and the fare is Rs {km_1*km*5 + 100}")



print("")




print("")


while True:

    Reached = input("Have you reached your destination? (yes/no)").lower()
    if Reached == "yes":
        print("Thank you for riding with rapido. Have a nice day.")
        break
    elif Reached == "no":
        print("Please reach your destination safely.")
