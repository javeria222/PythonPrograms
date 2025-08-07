#Slot Machine!!

import random

def spinRow():
    items = ["apple", "cherry", "grapes", "star", "sun"]
    
    return [random.choice(items) for item in range(3)]

def printRow(row):
    print("*********************")
    print(" | ".join(row))
    print("*********************")

def getpayout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "apple":
            return bet * 2
        elif row[0] == "cherry":
            return bet * 3
        elif row[0] == "grapes":
            return bet * 2
        elif row[0] == "star":
            return bet * 5
        elif row[0] == "sun":
            return bet * 4

    return 0


def main():
    balance = 100

    print("************************")
    print("Welcome to Slot Machine!")
    print("************************")

    while balance > 0:
        print(f"Current Balance: pkr{balance}")

        bet = input("Enter your bet amount: ")

        if not bet.isdigit():
            print("Please Enter a Valid Number!")
            continue
        bet = int(bet)

        if bet > balance:
            print("Insufficient Balance!")
        elif bet <= 0:
            print("Bet must be greater than zero!")
        else:
            balance -= bet
            row = spinRow()
            print("Spinning...\n")
            printRow(row)

            payout = getpayout(row, bet)

            if payout > 0:
                print(f"You Won pkr{payout}\n")
            else:
                print("Sorry you lost this round!\n")

            balance += payout
            playAgain = input("Do you want to play again? (Y/N): ").upper()

            if playAgain != "Y":
                print("**************************************************")
                print(f"  Game Over! Your final balance is pkr{balance}")
                print("**************************************************")
                break


if __name__ == '__main__':
    main()