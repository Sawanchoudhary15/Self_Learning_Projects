"""
Project: Student Attendance System
Rating: 9.2/10
Concepts: JSON (nested dicts) + PyInputPlus (inputDate, inputYesNo) + Menu loop
"""

import json
import pyinputplus as co
import os


def mark_attendance():
    choice_class = co.inputInt("Enter the class of student: ")
    student_name = co.inputStr("Enter the name of student: ")
    date = str(co.inputDate("Enter today's date: "))
    attendance = co.inputYesNo("Enter yes if present and no if not: ")

    filename = f"{choice_class}.txt"

    if os.path.exists(filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
        except:
            data = {}
    else:
        data = {}

    if student_name not in data:
        data[student_name] = {}

    data[student_name][date] = attendance

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print("✅ Attendance saved!")


def check_attendance():
    choice_class = co.inputInt("Enter the class of student: ")
    student_name = co.inputStr("Enter the name of student: ")
    specific = co.inputYesNo("You wants to check the attandance by date?: ")
    classes = f"{choice_class}.txt"

    if os.path.exists(classes):
        try:
            with open(classes, "r") as f:
                data = json.load(f)

            if student_name in data:
                if specific == "yes":
                    date = str(co.inputDate("Enter the date you wants to check the attandance: "))
                    if date in data[student_name]:
                        print(data[student_name][date])
                    else:
                        print("No record for this date")
                elif specific == "no":
                    print(data[student_name])

            elif student_name not in data:
                print(f"There is not student named {student_name} in this class")

        except:
            print("something not right")

    if os.path.exists(classes) == False:
        print("No such class is there in the school ")


def check_Student():
    choice_class = co.inputInt("Enter the class of student: ")
    student_name = co.inputStr("Enter the name of student: ")
    file = f"{choice_class}.txt"

    if os.path.exists(file):
        with open(file, "r") as f:
            data = json.load(f)
            if student_name in data:
                print("yeah the student is in this class")
            elif student_name not in data:
                print("No the student is not in this class")

    elif os.path.exists(file) == False:
        print("no such class is in the school")


if __name__ == '__main__':
    while True:
        choice = co.inputMenu(['mark attendance', 'check attendance', 'check student', "exit"])
        if choice == "mark attendance":
            mark_attendance()
        if choice == "check attendance":
            check_attendance()
        if choice == "check student":
            check_Student()
        if choice == "exit":
            break
