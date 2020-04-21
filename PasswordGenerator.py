# Password Generator
# Made by TheQuantumRobot

# ------- Modules -------

import random

# ------- Functions -------

# N/A

# ------- Main -------

print("Welcome to PassGen v.1.0\n------------------------")
print(
    "Instructions: PassGen is a tool to help generate strong passwords. \nPlease input the number of passwords you'd like to generate and number of characters."
)

while True:
    try:
        numPass = int(input("Number of Passwords: "))
        while (numPass <= 0) or (numPass >= 20):
            print("Please enter a number between zero and twenty!\n")
            numPass = int(input("Number of Passwords: "))
            continue
        break
    except ValueError:
        print("Please enter an number!")
while True:
    try:
        numChar = int(input("Number of Characters: "))
        while (numChar <= 0) or (numChar >= 20):
            print("Please enter a number between zero and twenty!\n")
            numChar = int(input("Number of Characters: "))
        break
    except ValueError:
        print("Please enter a number!")

specChar = ""
charNoSpec = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
charSpec = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!”#$%&’()*+-./\:;<=>?@[]^_`{|}~"

while specChar not in ("y", "n"):
    specChar = input("Special Characters? (Y/N): ").lower()

if specChar == "y":
    for c in range(numPass):
        password = ""
        for i in range(numChar):
            password += random.choice(charSpec)
        print(password)
else:
    for c in range(numPass):
        password = ""
        for i in range(numChar):
            password += random.choice(charNoSpec)
        print(password)
