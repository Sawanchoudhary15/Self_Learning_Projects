"""
Project: Contact Book
Rating: 9.7/10
Concepts: Dual-index data structure (inverted index) + regex validation 
          (name/phone/email) + re.fullmatch() auto-detection + JSON
"""

import json
import pyinputplus as co
import re


def load_data():
    try:
        with open("contact", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_data(data):
    with open("contact", "w") as f:
        json.dump(data, f, indent=4)


def add_contact():
    data = load_data()

    if "contacts_by_name" not in data:
        data["contacts_by_name"] = {}
    if "contacts_by_phone" not in data:
        data["contacts_by_phone"] = {}

    contacts_by_name = data["contacts_by_name"]
    contacts_by_phone = data["contacts_by_phone"]

    name = co.inputStr(
        "Enter name: ",
        allowRegexes=[r'^[A-Za-z ]+$'],
        blockRegexes=[(r'.*', "Only letters and spaces allowed")]
    ).title()

    phone = co.inputStr(
        "Enter phone: ",
        allowRegexes=[r'^[6-9]\d{9}$'],
        blockRegexes=[(r'.*', "Enter valid 10-digit phone number")]
    )

    email = co.inputStr(
        "Enter email: ",
        allowRegexes=[r'^[\w\.-]+@[\w\.-]+\.\w+$'],
        blockRegexes=[(r'.*', "Enter valid email")]
    )

    if phone in contacts_by_phone:
        print("Phone already exists ❌")
        return

    if name in contacts_by_name:
        choice = co.inputYesNo("Name exists. Update? (yes/no): ")
        if choice == "no":
            return
        old_phone = contacts_by_name[name]["phone"]
        del contacts_by_phone[old_phone]

    contacts_by_name[name] = {
        "phone": phone,
        "email": email
    }
    contacts_by_phone[phone] = name

    save_data(data)
    print("Contact saved successfully ✅")


def search_contact():
    data = load_data()
    contacts_by_name = data.get("contacts_by_name", {})
    contacts_by_phone = data.get("contacts_by_phone", {})

    choice = co.inputStr("Enter name or phone to search: ").title()

    if re.fullmatch(r'[6-9]\d{9}', choice):
        if choice in contacts_by_phone:
            name = contacts_by_phone[choice]
            info = contacts_by_name[name]
            print(f"\nName: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
        else:
            print("Phone not found ❌")

    elif re.fullmatch(r'[A-Za-z ]+', choice):
        if choice in contacts_by_name:
            info = contacts_by_name[choice]
            print(f"\nName: {choice}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
        else:
            print("Name not found ❌")
    else:
        print("Invalid input ❌")


def update_contact():
    data = load_data()
    choice = co.inputMenu(['update number', 'update name', 'update email', "exit"], numbered=True)
    contacts_by_name = data.get("contacts_by_name", {})
    contacts_by_phone = data.get("contacts_by_phone", {})

    if choice == 'update number':
        name = co.inputStr(
            "Enter name: ",
            allowRegexes=[r'^[A-Za-z ]+$'],
            blockRegexes=[(r'.*', "Only letters and spaces allowed")]).title()
        new_phone = co.inputStr(
            "Enter phone: ",
            allowRegexes=[r'^[6-9]\d{9}$'],
            blockRegexes=[(r'.*', "Enter valid 10-digit phone number")])

        if name in contacts_by_name:
            correction = contacts_by_name[name]
            no = correction["phone"]
            correction["phone"] = new_phone
            contacts_by_phone[f"{new_phone}"] = contacts_by_phone.pop(f"{no}")
            save_data(data)
            print("updated succesfulluy ")
        else:
            print("sorry but there is no contact with such name")

    elif choice == "update name":
        name = co.inputStr(
            "Enter name: ",
            allowRegexes=[r'^[A-Za-z ]+$'],
            blockRegexes=[(r'.*', "Only letters and spaces allowed")]).title()
        new_name = co.inputStr(
            "Enter new_name: ",
            allowRegexes=[r'^[A-Za-z ]+$'],
            blockRegexes=[(r'.*', "Only letters and spaces allowed")]).title()

        # NOTE: bug from original — check existence BEFORE accessing!
        if name in contacts_by_name:
            no = contacts_by_name[name]["phone"]
            contacts_by_name[f"{new_name}"] = contacts_by_name.pop(f"{name}")
            contacts_by_phone[no] = new_name
            save_data(data)
            print("data is successfully updated")
        else:
            print("there is no such contact here")

    elif choice == "update email":
        name = co.inputStr(
            "Enter name: ",
            allowRegexes=[r'^[A-Za-z ]+$'],
            blockRegexes=[(r'.*', "Only letters and spaces allowed")]).title()
        new_email = co.inputStr(
            "Enter email: ",
            allowRegexes=[r'^[\w\.-]+@[\w\.-]+\.\w+$'],
            blockRegexes=[(r'.*', "Enter valid email")])

        if name in contacts_by_name:
            contacts_by_name[name]["email"] = new_email
            save_data(data)
            print("successfully updated")
        else:
            print("these is no such data here")

    elif choice == "exit":
        print("thanks for using!")


def delete_contact():
    data = load_data()
    contacts_by_name = data.get("contacts_by_name", {})
    contacts_by_phone = data.get("contacts_by_phone", {})

    choice = co.inputStr("Enter name or phone to search and delete: ")

    if re.fullmatch(r'[6-9]\d{9}', choice):
        if choice in contacts_by_phone:
            name = contacts_by_phone[choice]
            contacts_by_name.pop(name, None)
            contacts_by_phone.pop(choice, None)
        else:
            print("Phone not found ❌")

    elif re.fullmatch(r'[A-Za-z ]+', choice):
        choice = choice.title()
        if choice in contacts_by_name:
            info = contacts_by_name[choice]["phone"]
            contacts_by_name.pop(choice, None)
            contacts_by_phone.pop(info, None)
        else:
            print("Name not found ❌")
    else:
        print("Invalid input ❌")

    save_data(data)


def view_contact():
    data = load_data()
    contacts = data.get("contacts_by_name", {})
    total_no = len(contacts.keys())

    for name, info in contacts.items():
        print(f"\n{name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")

    print(f"Total no of contact saved till now is {total_no} ")


def main_menu():
    while True:
        choice = co.inputMenu(
            ['Add Contact', 'Search Contact', 'Update Contact',
             'Delete Contact', 'List All', 'Exit'],
            numbered=True
        )
        if choice == 'Add Contact':
            add_contact()
        elif choice == 'Search Contact':
            search_contact()
        elif choice == 'Update Contact':
            update_contact()
        elif choice == 'Delete Contact':
            delete_contact()
        elif choice == 'List All':
            view_contact()
        elif choice == 'Exit':
            print("Goodbye 👋")
            break


if __name__ == '__main__':
    main_menu()
