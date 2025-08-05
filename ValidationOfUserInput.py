# Validate User Input
#1. User is no more than 12 characters
#2. User must not contain spaces
#3. User must not contain digits

#*** SIMPLE AND SHORTEST ANSWER! ***

#username = input("Enter your name: ")

#if len(username) <= 12 and username.isalpha():
 #   print(f"Your username is: {username}")
#else:
 #   print("Enter Valid Username..!!")


#*** PROPER EVENT HANDLING VIA DIFFERENT IF-ELSE STATEMENTS ***

username = input("Enter your name: ")
while True:
    if len(username) > 12:
        print("Username should be smaller than 12 characters")
        username = input("Enter your name: ")
    elif not username.find(" ") == -1:
        print("Username must not contain any spaces")
        username = input("Enter your name: ")
    elif not username.isalpha():
        print("Username must not contain any digits")
        username = input("Enter your name: ")
    else:
        print(f"Your username is: {username}")
        break