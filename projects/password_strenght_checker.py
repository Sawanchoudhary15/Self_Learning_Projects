import re
import pyinputplus as co


def password_Strength_checker():
    count = 0
    password = input("Enter a password: ")

    if len(password) >= 8:
        count += 1

    if any(letter.isupper() for letter in password):
        count += 1

    if any(letter.islower() for letter in password):
        count += 1

    if any(letter.isdigit() for letter in password):
        count += 1

    special = "!@#$%^&*"
    if any(letter in special for letter in password):
        count += 1

    print(count)

    if count == 5:
        print("very strong")
    elif count == 4:
        print("strong")
    elif count == 3:
        print("medium")
    elif count<=2:
        print("Weak")
    



password_Strength_checker()