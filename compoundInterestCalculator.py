# Python Compound Interest Calculator
# A = P( 1 + r/n )^t

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the amount of principle: "))
    if principle <= 0:
        print("Amount of principle can't be less than or equal to zero!")

while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest rate can't be less than or equal to zero!")

while time <= 0:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Time can't be less than or equal to zero!")

total = principle * pow((1 + rate / 100), time)
print(f"The total amount after {time} years is ${total:.2f}")