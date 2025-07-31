import math
#Circumference Of A Circle

radius = int(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
area = math.pi * pow(radius, 2)

print(f"Circumference of a circle is: {round(circumference)}")
print(f"Circumference of a circle is: {round(circumference, 2)}")
print(f"Area of the circle is: {round(area, 2)}")