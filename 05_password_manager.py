"""
Project: Password Manager
Rating: 9.3/10
Concepts: inputPassword + JSON + specific exceptions + menu loop
"""

import pyinputplus as co
import json


def Add_Password():
    site = co.inputStr("Enter the site name: ")
    password = co.inputPassword("Enter the password: ")

    try:
        with open("password_manager.txt", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    if site in data:
        choice = co.inputYesNo("Site exists. Overwrite? ")
        if choice == "yes":
            data[site] = password
    else:
        data[site] = password

    with open("password_manager.txt", "w") as f:
        json.dump(data, f, indent=4)


def List_All_Sites():
    try:
        with open("password_manager.txt", "r") as f:
            data = json.load(f)
            for key in data.keys():     # fixed from data.items() bug
                print(key)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No data found.")


def Delete_Password():
    site = co.inputStr("Enter the site name: ")

    try:
        with open("password_manager.txt", "r") as f:
            data = json.load(f)

        if site in data:
            print("Deleted:", data.pop(site))
            with open("password_manager.txt", "w") as f:
                json.dump(data, f, indent=4)
        else:
            print("No such site found.")

    except (FileNotFoundError, json.JSONDecodeError):
        print("No such file exists.")


if __name__ == '__main__':
    while True:
        choice = co.inputMenu(
            ["Add_Password", "List_All_Sites", "Delete_Password", "Exit"],
            numbered=True
        )
        if choice == "Add_Password":
            Add_Password()
        elif choice == "List_All_Sites":
            List_All_Sites()
        elif choice == "Delete_Password":
            Delete_Password()
        elif choice == "Exit":
            break
