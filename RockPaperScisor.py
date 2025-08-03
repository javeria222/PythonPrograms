# ROCK PAPER SCISSORS GAME PYTHON VERSION
import random

sysOpt = ("Rock", "Paper", "Scissor")

while True:
    userOpt = ""
    sys = random.choice(sysOpt)
    while userOpt not in sysOpt:
        userOpt = input("Enter your choice (Rock, Paper, Scissor): ").capitalize()

    if sys == userOpt:
        print(f"Computer choice {sys} : Your choice {userOpt}")
        print("ITS A TIE!")
    elif sys == "Rock" and userOpt == "Scissor":
        print(f"Computer choice {sys} : Your choice {userOpt}")
        print("YOUR LOSE!")
    elif sys == "Paper" and userOpt == "Rock":
        print(f"Computer choice {sys} : Your choice {userOpt}")
        print("YOUR LOSE!")
    elif sys == "Scissor" and userOpt == "Paper":
        print(f"Computer choice {sys} : Your choice {userOpt}")
        print("YOUR LOSE!")
    else:
        print(f"Computer choice {sys} : Your choice {userOpt}")
        print("YOUR WON!")

    if not input(("Play Again? (Y/N) ")).capitalize() == "Y":
        break
