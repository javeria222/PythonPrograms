# Validate User Input
#1. User is no more than 12 characters
#2. User must not contain spaces
#3. User must not contain digits

username = input("Enter your name: ")

if len(username) <= 12 and username.isalpha():
    print(f"Your username is: {username}")
else:
    print("Enter Valid Username..!!")

# FOR MORE SPECIFIC ADD DIFFERENT ELIF STATEMENTS AND PRINT MESSAGE ACCORDING TO IT