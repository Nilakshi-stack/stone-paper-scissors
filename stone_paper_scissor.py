import random

def sps():
    choices = ["stone", "paper", "scissors"]

    user = input("choose any one from stone,paper,scissor: ")
   

    if user not in choices:
        print("Invalid choice!")
        return

    computer = random.choice(choices)

    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a draw!")

    elif (user == "stone" and computer == "scissors") or (user == "paper" and computer == "stone") or (user == "scissors" and computer == "paper"):
        print("You win!")

    else:
        print("Computer wins!")