#Programming Quiz
questions = ["Q1. What lists are?",
             "Q2. What sets are?",
             "Q3. What tupples are?",
             "Q4. Which one is not a valid varieble name",
             "Q5. What is the output of varieble.upper() method?"]
options = [("A. Ordered", "B. Unordered", "C. Changeable", "D. Both A and C"),
          ("A. Ordered", "B. Unordered", "C. Changeable", "D. Both A and C"),
          ("A. Ordered", "B. Unordered", "C. Changeable", "D. Both A and C"),
          ("A. varieble_name", "B. varieble name", "C. VariebleName", "D. varieble123"),
          ("A. First character will become capital", "B. First character will become smaller", "C. All Capatalized", "D. Both A and C")]
answers = ("D", "B", "A", "B", "D")
guesses = []
optNum = 0
score = 0

for x in questions:
    print(x)
    for y in options[optNum]:
        print(y)

    guess = input("Enter your answer(A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[optNum]:
        print("CORRECT!")
        score += 1
    else:
        print("INCORRECT!")
    optNum += 1
    print("--------------------------------")

print("================== RESULT ====================")
for ans in answers:
    print(f"Correct Answers: {ans}", end=" ")
print()
for gss in guesses:
    print(f"Your Answers: {gss}", end=" ")
print()

score = score / len(questions) * 100
print(f"Your score is: {score}%")
print("===============================================")