#Hangman Game

import random

# Can add more words or make a seperate file for words and import that file to use those words!!
words = ["apple", "banana", "cherry", "grapes", "cocunut", "orange"]

hangman = {0:("     ",
              "     ",
              "     "),
           1: ("  o  ",
               "     ",
               "     "),
           2: ("  o  ",
               "  |  ",
               "     "),
           3: ("  o  ",
               " /|  ",
               "     "),
           4: ("  o  ",
               " /|\\",
               "     "),
           5: ("  o  ",
               " /|\\",
               " /   "),
           6: ("  o  ",
               " /|\\",
               " / \\")}

def displayMan(wrongGuesses):
    print("**********")
    for line in hangman[wrongGuesses]:
        print(f"  {line}")
    print("**********")

def displayHint(hint):
    print(" ".join(hint))

def displayAns(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrongGuesses = 0
    guessedLetters = set()

    while True:
        displayMan(wrongGuesses)
        displayHint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) > 1 or not guess.isalpha():
            print("Invalid Output!")
            continue

        if guess in guessedLetters:
            print(f"{guess} is already guessed!")
            continue

        guessedLetters.add(guess)


        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        else:
            wrongGuesses += 1

        if "_" not in hint:
            displayMan(wrongGuesses)
            displayAns(answer)
            print("YOU WON!!")
            break
        elif wrongGuesses >= len(hangman) - 1:
            displayMan(wrongGuesses)
            displayAns(answer)
            print("YOU LOSE!!")
            break

if __name__ == '__main__':
    main()