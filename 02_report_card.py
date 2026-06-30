"""
Project: Student Report Card Generator
Rating: 9.0/10
Concepts: Regex (blockRegexes) + PyInputPlus + Shelve + Grading logic
"""

import shelve
import pyinputplus as co
from pathlib import Path as path

def enter():
    folder = path(__file__).parent
    name = co.inputStr(
        "Enter the name without spaces use underscore instead: ",
        blockRegexes=[r"[0-9\s]"]
    )
    print(name)
    with shelve.open(str(folder / f"{name}.txt")) as f:
        f["enlish"] = co.inputNum("enter the marks of enlish: ", min=0, max=100)
        f["maths"] = co.inputNum("enter the marks of maths: ", min=0, max=100)
        f["sst"] = co.inputNum("enter the marks of sst: ", min=0, max=100)
        f["computer"] = co.inputNum("enter the marks of computere: ", min=0, max=100)
        f["physics"] = co.inputNum("enter the marks of physics: ", min=0, max=100)
        total = sum(list(f.values()))
        f['total'] = total
        percentage = total / 5
        f['percentage'] = percentage

        if percentage >= 90:
            print("Grade: A+")
            f['grade'] = "A+"
        elif percentage >= 80:
            print("Grade: A")
            f['grade'] = "A"
        elif percentage >= 70:
            print("Grade: B")
            f['grade'] = "B"
        elif percentage >= 60:
            print("Grade: C")
            f['grade'] = "C"
        elif percentage >= 50:
            print("Grade: D")
            f['grade'] = "D"
        else:
            print("Grade: F")
            f['grade'] = "F"


def seeing_result():
    name = co.inputStr(
        "enter the name of the sudent you wants to find out the result of: ",
        blockRegexes=[r"[0-9\s]"]
    )
    folder = path(__file__).parent
    new = folder / f'{name}.txt'
    check = new.exists()
    if check == True:
        with shelve.open(str(folder / f"{name}.txt")) as f:
            for key, value in f.items():
                print(key, value)
    else:
        print("no entry under that name sir sorry : ")


if __name__ == '__main__':
    enter()
    seeing_result()
