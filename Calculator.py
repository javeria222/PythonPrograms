#Python Calculator

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
operator = input("Enter an Operator (+,-,*,/): ")

if operator == "+":
    print(f"Result is: {round(num1 + num2, 2)}")
elif operator == "*":
    print(f"Result is: {round(num1 * num2, 2)}")
elif operator == "-":
    print(f"Result is: {round(num1 - num2, 2)}")
elif operator == "/":
    print(f"Result is: {round(num1 / num2, 2)}")
else:
    print("Enter a valid operator sign!")