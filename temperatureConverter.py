#Temperature Converter

unit = input("Enter the unit of temperature(C/F): ")
temp = float(input("Enter Temperature: "))

if unit == "C":
    temp = (temp * 9/5) + 32
    unit = "F"
    print(f"Entered Temperature in Farhenhiet is: {temp} {unit}")
elif unit == "F":
    temp = (temp - 32) * 5/9
    unit = "C"
    print(f"Entered Temperature in Celsius is: {temp} {unit}")
else:
    print("Enter valid unit of temperature!")