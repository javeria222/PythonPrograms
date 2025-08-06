#Simple Banking program to check, deposit and withdraw balance using Python
name = "Ahmed"
acountNum = "ahm123"
balance = 1500000

def showBalance():
    print(f"Name: {name}")
    print(f"Acount Number: {acountNum}")
    print(f"Blance: {balance}")
    print("***********************")

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        showBalance()
    else:
        print("Please enter a valid amount to deposit")
        print("***********************")



def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient Balance")
        print("***********************")
    elif amount < 0:
        print("Please enter a valid amount to withdraw")
        print("***********************")
    else:
        balance -= amount
        showBalance()


def bankingOptions(opt):
    match opt:
        case 1:
            return showBalance()
        case 2:
            return deposit()
        case 3:
            return withdraw()
        case 4:
            return print("Thanks for using our Bank!")
        case _:
            return print("Please select a valid option!")

def main():
    print("----- Banking System -----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("--------------------------")

if __name__ == '__main__':
    while True:
        print()
        main()
        print()
        opt = int(input("Please select a number to to proceed: "))
        bankingOptions(opt)
        if opt == 4:
            print(" ***********************")
            break