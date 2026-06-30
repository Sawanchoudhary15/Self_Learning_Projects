"""
Project: Personal Expense Tracker
Rating: 9.5/10
Concepts: inputMonth + calendar module + load_data/save_data pattern (DRY)
"""

import pyinputplus as co
import json
import calendar


def load_data():
    try:
        with open("expense.txt", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_data(data):
    with open("expense.txt", "w") as f:
        json.dump(data, f, indent=4)


def add_expenses():
    data = load_data()
    month_num = co.inputMonth("Enter the month: ")
    month = calendar.month_name[month_num]
    if month not in data:
        data[month] = {}
    while True:
        item = co.inputStr("Enter item name: ")
        expense = co.inputFloat("Enter amount: ", min=0)
        if item in data[month]:
            choice = co.inputYesNo(
                "Item exists. Add to existing? (yes/no): "
            )
            if choice == "yes":
                data[month][item] += expense
        else:
            data[month][item] = expense
        save_data(data)
        if co.inputYesNo("Add more? (yes/no): ") == "no":
            break


def view_expense():
    data = load_data()
    month_num = co.inputMonth("Enter the month: ")
    month = calendar.month_name[month_num]
    if month in data:
        print(f"\nExpenses for {month}:\n")
        for item, amount in data[month].items():
            print(f"{item} = {amount}")
        total = sum(data[month].values())
        print(f"\nTotal spending: {total}")
    else:
        print("No data for this month")


def main():
    while True:
        choice = co.inputMenu(
            ["Add Expense", "View Expense", "Exit"],
            numbered=True
        )
        if choice == "Add Expense":
            add_expenses()
        elif choice == "View Expense":
            view_expense()
        elif choice == "Exit":
            print("Goodbye 👋")
            break


if __name__ == '__main__':
    main()
