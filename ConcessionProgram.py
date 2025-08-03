#Concession Stand Program

menu = {"Pizza": 500,
        "Burger": 400,
        "Popcorn": 100,
        "Biryani": 300,
        "Pulao": 250,
        "Macaroni": 200,
        "Fries": 150}

print("========= Menu =========")
for key, value in menu.items():
    print(f" {key:10} ------ {value}")
print("========================")

orders = []
total = 0

while True:
    order = input("Enter your item to place order (Q to exit): ").capitalize()
    if order == "Q":
        break
    elif menu.get(order) is not None:
        orders.append(order)
    else:
        print("This item is not in the menu.")

print("--------- YOUR ORDER ---------")
for order in orders:
    total += menu.get(order)
    print(order)

print("------------------------------")
print(f"Total is: {total}pkr")
print("------------------------------")
