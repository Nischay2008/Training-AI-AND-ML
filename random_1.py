import random

options = ["rock", "paper", "scissors"]


def main():
    Computer_Score = 0
    User_Score = 0

    while True:
        computer_choice = random.choice(options)
        user_choice = input(
            "Enter your choice (Rock/Paper/Scissors): ").lower()

        if user_choice not in options:
            print("Invalid entry. Please enter Rock, Paper, or Scissors.")
            continue

        print(f"Computer chose: {computer_choice}")

        result = verify(computer_choice, user_choice)

        if result == "computer":
            Computer_Score += 1
            print("Computer wins this round!")
        elif result == "user":
            User_Score += 1
            print("You win this round!")
        else:
            print("It’s a tie.")

        print(f"Score --> Computer: {Computer_Score} | You: {User_Score}\n")

        if Computer_Score >= 3:
            print("Computer won the game!")
            break
        elif User_Score >= 3:
            print("You won the game!")
            break

    print("Game Over. Thanks for playing!")


def verify(computer, user):
    if computer == user:
        return "tie"
    elif (computer == 'rock' and user == 'scissors') or \
         (computer == 'paper' and user == 'rock') or \
         (computer == 'scissors' and user == 'paper'):
        return "computer"
    else:
        return "user"


main()
