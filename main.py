# Rectangular Area Calculation
import math

width = int(input("Enter width of a rectangle: "))
height = int(input("Enter height of a rectangle: "))

area = width * height

print (f"Area of the rectangle is: {area}")

# Shopping Cart
item = input("What do you want to order? ")
price = float(input("What is the price of the item? "))
item = int(input("What is the quantity of the item? "))

total_bill = price * item
print(f"Your total bill of item {item} is: {total_bill}")

# Math Functions
#round, abs, pow, max, min
result1 = pow(4, 3)
result2 = 4**3

print(round(3.8)) #4
print(int(3.8)) #3
print(math.ceil(3.8)) #4
print(math.floor(3.8)) #3

print(result1)
print(result2)