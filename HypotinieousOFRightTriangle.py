import math
#Hypotenious of right triangle
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Hypotenioues of Right Angle Triangle is: {round(c, 2)}")