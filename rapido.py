import random
import time

def main():
    class Colors:

        RESET = '\033[0m'
        RED = '\033[91m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        BLUE = '\033[94m'
        MAGENTA = '\033[95m'
        CYAN = '\033[96m'
        WHITE = '\033[97m'
        BRIGHT_YELLOW = '\033[93;1m'

    color_cycle = [
        Colors.RED,
        Colors.GREEN,
        Colors.BLUE,
        Colors.MAGENTA,
        Colors.CYAN,
        Colors.BRIGHT_YELLOW,
        Colors.WHITE
    ]

    print(f"{Colors.BRIGHT_YELLOW}Welcome to rapido app.{Colors.RESET}")
    delay_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    users = ["Nischay", "Vinay", "Hasini", "Rohith"]
    passwords = ["Nischay@123", "Vinay@123", "Hasini@123", "Rohith@123"]
    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    num1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    alpha = ["a", "b", "c", "d", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]
    alpha_c = ["A", "B", "C", "D", "F", "G", "H", "I", "J", "K", "L",
            "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]
    special = ["@", "#", "$", "&", "=", "+", "!"]
    lang = ["english", "telugu", "hindi"] 
    delay = random.choices(delay_x)
    bike = True
    car = True
    ac_car = True
    surge = True
    km_1 = 20
    
    print("")
    while True:
        Language = input(
        f"{Colors.BLUE}Please choose the language.{Colors.RESET} {Colors.BLUE}(English , Telugu , Hindi): {Colors.RESET}").lower()
        if Language in lang:
           break
        else:
            print(f"{Colors.RED}Wrong input. Try again.{Colors.RESET}")
    while True:
        x = input(f"{Colors.GREEN}Enter your user:{Colors.RESET}").capitalize()
        if x in users:
            break
        else:
            print(f"{Colors.RED}Invalid User try again.{Colors.RESET}")
    while True:
        y = input(f"{Colors.GREEN}Enter your password:{Colors.RESET}").capitalize()
        if y in passwords:
            break
        else:
            print(f'{Colors.RED}Invalid password.{Colors.RESET}')
    while True  :
        rnum = random.choice(num)
        ralp = random.choice(alpha)
        rnum1 = random.choice(num1)
        rspe = random.choice(special)
        ralpc = random.choice(alpha_c)
        captcha = rnum+ralp+rnum+rspe+ralpc
        print(f"{Colors.GREEN}Rewrite the Captcha :{Colors.RESET} {captcha}")
        x = input(f"{Colors.BLUE}Enter the captcha: {Colors.RESET}")
        if x == captcha:
            print(f"{Colors.GREEN}Correct{Colors.RESET}")
            break
        else:
            print(f"{Colors.RED}Incorrect. Try again.{Colors.GREEN}")
    while True:
        otp = random.randint(10000,99999)
        print(f"Your test OTP is {otp}")
        z = int(input(f"{Colors.GREEN}Enter a OTP: {Colors.RESET}"))
        if z == otp:
            break
        else:
            print(f"{Colors.RED}Invalid OTP{Colors.RESET}")
    print(f"{Colors.GREEN}You have logged in{Colors.RESET}")
    Ride = ["bike", "car", "ac_car", "parcel"]
    drop = input(f"{Colors.GREEN}Please enter your drop location{Colors.RESET}")
    km = int(input(f"{Colors.GREEN}Please enter the distance in KM's{Colors.RESET}"))
    while True:
        vec = input(
            f"{Colors.YELLOW}Please enter the ride you choose from the list.(Bike , Car, AC_car , Parcel){Colors.RESET}").lower()
        if vec in Ride:
            break
        else:
            print(f"{Colors.RED}Invalid, Try again.{Colors.RESET}")
    if vec == "bike":
        print(f"{Colors.BRIGHT_YELLOW}You have chosen bike. Your ride is on the way.{Colors.RESET}")
        print(
            f"{Colors.YELLOW}Your ride will arrive in {delay} minutes and the fare is Rs {km_1*km*0.5}{Colors.RESET}")
    elif vec == "Parcel":
        enter = input(f"{Colors.GREEN}Enter the area you wanna send it to.{Colors.RESET}")
        print(
            f"{Colors.YELLOW}The parcel order has been confirmed. Your price is {km_1*km + 100}{Colors.RESET}")
    elif surge == True and vec == "bike":
        print(f"{Colors.YELLOW}You have chosen bike. Your ride is on the way.{Colors.RESET}")
        print(
            f"{Colors.YELLOW}Your ride will arrive in {delay} minutes and the fare is Rs {km_1*km*0.5 + 10}{Colors.RESET}")
    if vec == "car":
        print(f"{Colors.YELLOW}You have chosen car. Your ride is on the way.{Colors.RESET}")
        print(
            f"{Colors.YELLOW}Your ride will arrive in {delay} minutes and the fare is Rs {km_1*km*2}{Colors.YELLOW}")
    elif surge == True and vec == "car":
        print(f"{Colors.YELLOW}You have chosen car. Your ride is on the way.{Colors.YELLOW}")
        print(
            f"{Colors.YELLOW}Your ride will arrive in {delay} minutes and the fare is Rs {km_1*km*2 + 30}{Colors.RESET}")
    if vec == "ac_car":
        print(f"{Colors.YELLOW}You have chosen ac-car. Your ride is on the way.{Colors.RESET}")
        print(
            f"Your ride will arrive in {delay} minutes and the fare is Rs {km_1*km*5}")
    elif surge == True and vec == "ac-car":
        print("You have chosen ac-car. Your ride is on the way.")
        print(
            f"Your ride will arrive in {delay} minutes and the fare is Rs {km_1*km*5 + 100}")
    while True:
        Reached = input(f"{Colors.BRIGHT_YELLOW}Have you reached your destination? (yes/no): {Colors.RESET}").lower()
        if Reached == "yes":
            print(f"{Colors.GREEN}Thank you for riding with {Colors.BRIGHT_YELLOW}Rapido{Colors.RESET}.{Colors.GREEN} Have a nice day.{Colors.RESET}")
            break
        elif Reached == "no":
            print(f"{Colors.RED}Please reach your destination safely.{Colors.RESET}")
        time.sleep(2)
    # while True:
    #     inp = input("Wanna enter the app again: Type Enter: ").capitalize()
    #     if Reached == "Enter":
    #         return main()
    #     else:
    #         break
main()
