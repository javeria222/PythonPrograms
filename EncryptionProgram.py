#Encryption and Decryption Program

import string
import random

chars = string.digits + string.ascii_letters + string.punctuation + " "
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"Chars: {chars}")
#print(f"Key: {key}")

#ENCRYPTION
plainText = input("Enter a message to Encrypt: ")
encrypted = ""

for letter in plainText:
    index = chars.index(letter)
    encrypted += key[index]

print(f"Original Message : {plainText}")
print(f"Encrypted Message: {encrypted}")

#ENCRYPTION
encrypted = input("Enter a message to Decrypt: ")
decrypted = ""

for letter in encrypted:
    index = key.index(letter)
    decrypted += chars[index]

print(f"Encrypted Message: {encrypted}")
print(f"Decrypted Message: {decrypted}")
