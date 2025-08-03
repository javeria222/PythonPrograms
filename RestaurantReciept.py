#Restaurant Reciept Program

foods = []
prices = []
total = 0

while True:
    food = input("Enter the food you want to buy (q to exit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of the {food}: pkr "))
        foods.append(food)
        prices.append(price)
        total += price

print(" ==============RECEIPT===============")
for x in foods:
    print(x, end=" ")
print()
for y in prices:
    print(y, end="   ")
print()
print(f"Your total bill is: {total}pkr")
